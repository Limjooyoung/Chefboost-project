import pathlib
import os
from os import path
import multiprocessing
import CB as cb


def bulk_prediction(df, model):
    predictions = []

    for index, instance in df.iterrows():
        features = instance.values[0:-1]
        prediction = cb.predict(model, features)
        predictions.append(prediction)

    df['Prediction'] = predictions


def initializeFolders():
    import sys
    sys.path.append("..")
    pathlib.Path("outputs").mkdir(parents=True, exist_ok=True)
    pathlib.Path("outputs/data").mkdir(parents=True, exist_ok=True)
    pathlib.Path("outputs/rules").mkdir(parents=True, exist_ok=True)

    # -----------------------------------

    # clear existing rules in outputs/

    outputs_path = os.getcwd() + os.path.sep + "outputs" + os.path.sep

    try:
        if path.exists(outputs_path + "data"):
            for file in os.listdir(outputs_path + "data"):
                os.remove(outputs_path + "data" + os.path.sep + file)

        if path.exists(outputs_path + "rules"):
            for file in os.listdir(outputs_path + "rules"):
                if ".py" in file or ".json" in file or ".txt" in file or ".pkl" in file or ".csv" in file:
                    os.remove(outputs_path + "rules" + os.path.sep + file)
    except Exception as err:
        print("WARNING: ", str(err))


# ------------------------------------

def initializeParams(config):
    algorithm = 'ID3'
    enableRandomForest = False
    num_of_trees = 5
    enableMultitasking = False
    enableGBM = False
    epochs = 10
    learning_rate = 1
    max_depth = 3
    enableAdaboost = False
    num_of_weak_classifier = 4
    enableParallelism = True
    num_cores = int(multiprocessing.cpu_count() / 2)  # allocate half of your total cores

    # 코어의 개수를 왜 /2했을까?

    # num_cores = int((3*multiprocessing.cpu_count())/4) #allocate 3/4 of your total cores
    # num_cores = multiprocessing.cpu_count()

    for key, value in config.items():
        if key == 'algorithm':
            algorithm = value
        # ---------------------------------
        elif key == 'enableRandomForest':
            enableRandomForest = value
        elif key == 'num_of_trees':
            num_of_trees = value
        elif key == 'enableMultitasking':
            enableMultitasking = value
        # ---------------------------------
        elif key == 'enableGBM':
            enableGBM = value
        elif key == 'epochs':
            epochs = value
        elif key == 'learning_rate':
            learning_rate = value
        elif key == 'max_depth':
            max_depth = value
        # ---------------------------------
        elif key == 'enableAdaboost':
            enableAdaboost = value
        elif key == 'num_of_weak_classifier':
            num_of_weak_classifier = value
        # ---------------------------------
        elif key == 'enableParallelism':
            enableParallelism = value
        elif key == 'num_cores':
            num_cores = value

    config['algorithm'] = algorithm
    config['enableRandomForest'] = enableRandomForest
    config['num_of_trees'] = num_of_trees
    config['enableMultitasking'] = enableMultitasking
    config['enableGBM'] = enableGBM
    config['epochs'] = epochs
    config['learning_rate'] = learning_rate
    config['max_depth'] = max_depth
    config['enableAdaboost'] = enableAdaboost
    config['num_of_weak_classifier'] = num_of_weak_classifier
    config['enableParallelism'] = enableParallelism
    config['num_cores'] = num_cores

    return config


def createFile(file,content):
    f = open(file, "w")
    f.write(content)