def findDecision(obj): #obj[0]: fixed acidity, obj[1]: volatile acidity, obj[2]: citric acid, obj[3]: residual sugar, obj[4]: chlorides, obj[5]: free sulfur dioxide, obj[6]: total sulfur dioxide, obj[7]: density, obj[8]: pH, obj[9]: sulphates, obj[10]: alcohol
	# {"feature": "alcohol", "instances": 1199, "metric_value": 0.9953, "depth": 1}
	if obj[10]<=11.509215380395142:
		# {"feature": "total sulfur dioxide", "instances": 1013, "metric_value": 0.9979, "depth": 2}
		if obj[6]<=113.16795074109501:
			# {"feature": "volatile acidity", "instances": 960, "metric_value": 0.9999, "depth": 3}
			if obj[1]<=1.0873108255535033:
				# {"feature": "fixed acidity", "instances": 952, "metric_value": 1.0, "depth": 4}
				if obj[0]>5.0:
					# {"feature": "chlorides", "instances": 950, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.038:
						# {"feature": "citric acid", "instances": 948, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0.8411449131956559:
							# {"feature": "sulphates", "instances": 947, "metric_value": 1.0, "depth": 7}
							if obj[9]>0.33:
								# {"feature": "free sulfur dioxide", "instances": 946, "metric_value": 1.0, "depth": 8}
								if obj[5]>1.0:
									# {"feature": "density", "instances": 945, "metric_value": 1.0, "depth": 9}
									if obj[7]>0.99236:
										# {"feature": "pH", "instances": 944, "metric_value": 1.0, "depth": 10}
										if obj[8]>2.87:
											# {"feature": "residual sugar", "instances": 943, "metric_value": 1.0, "depth": 11}
											if obj[3]<=6.683584361219497:
												return 'bad'
											elif obj[3]>6.683584361219497:
												return 'good'
											else: return 'good'
										elif obj[8]<=2.87:
											return 'good'
										else: return 'good'
									elif obj[7]<=0.99236:
										return 'good'
									else: return 'good'
								elif obj[5]<=1.0:
									return 'good'
								else: return 'good'
							elif obj[9]<=0.33:
								return 'bad'
							else: return 'bad'
						elif obj[2]>0.8411449131956559:
							return 'bad'
						else: return 'bad'
					elif obj[4]<=0.038:
						return 'good'
					else: return 'good'
				elif obj[0]<=5.0:
					return 'bad'
				else: return 'bad'
			elif obj[1]>1.0873108255535033:
				return 'bad'
			else: return 'bad'
		elif obj[6]>113.16795074109501:
			# {"feature": "pH", "instances": 53, "metric_value": 0.3138, "depth": 3}
			if obj[8]>2.93:
				# {"feature": "residual sugar", "instances": 52, "metric_value": 0.2352, "depth": 4}
				if obj[3]<=7.150143121415109:
					# {"feature": "volatile acidity", "instances": 48, "metric_value": 0.1461, "depth": 5}
					if obj[1]<=0.5754166666666666:
						return 'bad'
					elif obj[1]>0.5754166666666666:
						# {"feature": "chlorides", "instances": 24, "metric_value": 0.2499, "depth": 6}
						if obj[4]>0.066:
							return 'bad'
						elif obj[4]<=0.066:
							return 'good'
						else: return 'good'
					else: return 'bad'
				elif obj[3]>7.150143121415109:
					# {"feature": "volatile acidity", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0.42:
						return 'bad'
					elif obj[1]<=0.42:
						return 'good'
					else: return 'good'
				else: return 'bad'
			elif obj[8]<=2.93:
				return 'good'
			else: return 'good'
		else: return 'bad'
	elif obj[10]>11.509215380395142:
		# {"feature": "fixed acidity", "instances": 186, "metric_value": 0.4411, "depth": 2}
		if obj[0]>4.6:
			# {"feature": "citric acid", "instances": 185, "metric_value": 0.4246, "depth": 3}
			if obj[2]<=0.7554627194077835:
				# {"feature": "pH", "instances": 183, "metric_value": 0.4091, "depth": 4}
				if obj[8]>2.989586109723027:
					# {"feature": "sulphates", "instances": 181, "metric_value": 0.3928, "depth": 5}
					if obj[9]<=0.6772375690607733:
						# {"feature": "volatile acidity", "instances": 96, "metric_value": 0.5993, "depth": 6}
						if obj[1]<=0.4758854166666668:
							# {"feature": "residual sugar", "instances": 52, "metric_value": 0.2352, "depth": 7}
							if obj[3]<=4.634310933933659:
								# {"feature": "density", "instances": 46, "metric_value": 0.1511, "depth": 8}
								if obj[7]<=0.9964833869231186:
									return 'good'
								elif obj[7]>0.9964833869231186:
									# {"feature": "free sulfur dioxide", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[5]<=9.0:
										return 'good'
									elif obj[5]>9.0:
										# {"feature": "chlorides", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]>0.085:
											return 'good'
										elif obj[4]<=0.085:
											return 'bad'
										else: return 'bad'
									else: return 'good'
								else: return 'good'
							elif obj[3]>4.634310933933659:
								# {"feature": "free sulfur dioxide", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[5]>3.0:
									return 'good'
								elif obj[5]<=3.0:
									# {"feature": "chlorides", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0.05:
										return 'bad'
									elif obj[4]>0.05:
										return 'good'
									else: return 'good'
								else: return 'good'
							else: return 'good'
						elif obj[1]>0.4758854166666668:
							# {"feature": "residual sugar", "instances": 44, "metric_value": 0.8454, "depth": 7}
							if obj[3]<=6.049812829187187:
								# {"feature": "free sulfur dioxide", "instances": 43, "metric_value": 0.8204, "depth": 8}
								if obj[5]>6.0:
									# {"feature": "chlorides", "instances": 36, "metric_value": 0.888, "depth": 9}
									if obj[4]>0.040999999999999995:
										# {"feature": "density", "instances": 34, "metric_value": 0.9082, "depth": 10}
										if obj[7]>0.992441985831979:
											# {"feature": "total sulfur dioxide", "instances": 31, "metric_value": 0.9383, "depth": 11}
											if obj[6]>16.0:
												return 'good'
											elif obj[6]<=16.0:
												return 'bad'
											else: return 'bad'
										elif obj[7]<=0.992441985831979:
											return 'good'
										else: return 'good'
									elif obj[4]<=0.040999999999999995:
										return 'good'
									else: return 'good'
								elif obj[5]<=6.0:
									return 'good'
								else: return 'good'
							elif obj[3]>6.049812829187187:
								return 'bad'
							else: return 'bad'
						else: return 'good'
					elif obj[9]>0.6772375690607733:
						return 'good'
					else: return 'good'
				elif obj[8]<=2.989586109723027:
					# {"feature": "volatile acidity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0.18:
						return 'good'
					elif obj[1]>0.18:
						return 'bad'
					else: return 'bad'
				else: return 'good'
			elif obj[2]>0.7554627194077835:
				# {"feature": "volatile acidity", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0.37:
					return 'bad'
				elif obj[1]<=0.37:
					return 'good'
				else: return 'good'
			else: return 'good'
		elif obj[0]<=4.6:
			return 'bad'
		else: return 'bad'
	else: return 'good'
