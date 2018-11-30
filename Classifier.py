import random
import math
import operator

training_set = []
test_set = []


# controller method for knn
def knn_controller(full_data):

  print("Beginning classification training... ")

  # holds accuracy data
  total_predictions = 0
  total_pos = 0
  total_users = 0
  total_caught = 0
  total_false_pos = 0
  total_missed = 0

  # split into test and training
  for student in full_data:
    if random.random() < 0.67:
      training_set.append(student.get_risk_factors())
    else:
      test_set.append(student.get_risk_factors())

  for i in range (0, len(test_set)):
    total_predictions += 1
    usage_prediction = make_prediction(test_set[i])
    
    outcome = False
    
    if test_set[i][0] == 2:
      outcome = True

    if outcome == True:
      total_users += 1
    
    if usage_prediction == True:
      total_pos += 1

    if outcome == True and usage_prediction == outcome:
      total_caught += 1

    if outcome == False and usage_prediction == True:
      total_false_pos += 1

    if outcome == True and usage_prediction == False:
      total_missed += 1

    if i > 200:
      # run accuracy stats
      print("\n\n" + str((total_caught / total_users)*100) + "% of users detected.")
      print(str((total_caught / total_users - 1)*(-100)) + "% of users not detected.")
      print(str((total_false_pos / total_pos)*100) + "% of positive predictions were false positives.")
      print(str((total_users/total_predictions)*100) + "% of the sample were users.")

  pass


def euclidean_distance(instance1, instance2, length):
    distance = 0
    # opiate use is index 0.
    for x in range(1, length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# returns array of closest neighbors
def get_neighbors(test_instance, k):
    distances = []
    length = len(test_instance)

    for x in range(0, len(training_set)):
      dist = euclidean_distance(test_instance, training_set[x], length)
      distances.append((training_set[x], dist))

    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for x in range(k):
      neighbors.append(distances[x][0])
    return neighbors
    pass

# makes prediciton
def get_prediction_abuse(neighbors):
  user = 0
  clean = 0
  for x in range(len(neighbors)):
    if neighbors[x][-1] == 1:
      clean += 1
    else:
      user += 1

  return user / (user + clean)

# 49, 63 @20 | 50, 58 @ 25 | 

def make_prediction(test_instance):
    k = 20 
    neighbors = get_neighbors(test_instance, k)

    abuse_probability = get_prediction_abuse(neighbors)

    score = test_instance[1]

    print("Estimated probabiltiy: " + str(abuse_probability) + ", Actual: " + str(test_instance[0]-1) + " Score: " + str(test_instance[1]))

    if (abuse_probability >= 0.05 and score >= 6) or (score >= 8):
        return True
    else:
        return False




### =========================================== ###

# controller method for naive bayes classifier
def naive_bayes_controller(full_data):

  print("Beginning classification training... ")

  # holds accuracy data
  total_predictions = 0
  total_pos = 0
  total_users = 0
  total_caught = 0
  total_false_pos = 0
  total_missed = 0

  # split into test and training
  test_set = []
  training_set = []

  users = []
  non_users = []

  total = 0

  for student in full_data:
    if random.random() < 0.67:
      training_set.append(student.get_risk_factors())
    else:
      test_set.append(student.get_risk_factors())

  for profile in training_set:
    total += 1
    if profile[0] == 2:
      users.append(profile)

    else:
      non_users.append(profile)

  user_means = []
  user_stdevs = []

  non_user_means = []
  non_user_stdevs = []

  # user data
  user_class_values = []
  for i in range(0, len(users[0])-1):
    user_class_values.append([])

  for student in users:
    for value in range(1, len(student)):
      user_class_values[value-1].append(student[value])

  # non-user data  
  non_user_class_values = []
  for i in range(0, len(non_users[0])-1):
    non_user_class_values.append([])

  for student in non_users:
    for value in range(1, len(student)):
      non_user_class_values[value-1].append(student[value])

  # calculate means & stdevs
  for valueset in user_class_values:
    user_means.append(mean(valueset)) 

  for valueset in non_user_class_values:
    non_user_means.append(mean(valueset))  
    
  for valueset in user_class_values:
    user_stdevs.append(stdev(valueset)) 
     
  for valueset in non_user_class_values:
    non_user_stdevs.append(stdev(valueset))

  user_mean = 0
  user_stdev = 0
  non_user_mean = 0
  non_user_stdev = 0

  # make prediction
  for profile in test_set:

    max_prob = 0
    outcome_pred = 0  # 0 for clean, 1 for user

    # attempt to use the strongest probability of belonging to class clean or user
    for i in range(1, len(profile)):
      user_probability = calculateProbability(profile[i], user_means[i-1], user_stdevs[i-1])
      clean_probability = calculateProbability(profile[i], non_user_means[i-1], non_user_stdevs[i-1])
      if user_probability >= max_prob:
        max_prob = user_probability
        outcome_pred = 1
      if clean_probability > max_prob:
        max_prob = clean_probability
        outcome_pred = 0

      if i == 1:
        user_mean = user_means[i-1]
        user_stdev = user_stdevs[i-1]
        non_user_mean = non_user_means[i-1]
        non_user_stdev = non_user_stdevs[i-1]

    is_user = "NO"
    if (profile[0] == 2):
      is_user = "YES"

    prediction = "NOT BEING"
    if (outcome_pred == 1):
      prediction = "BEING"

    print("STUDENT is predicted as: " + prediction + " a user, with a risk score of: " + str(profile[0]))
    print("STUDENT is user? " + is_user)

    total_predictions += 1

    if is_user == "YES":
      total_users += 1

    if prediction == "BEING":
      total_pos += 1
    
    if prediction == "BEING" and is_user == "YES":
      total_caught += 1
    if prediction == "BEING" and is_user == "NO":
      total_false_pos += 1
    if prediction == "NOT BEING" and is_user == "YES":
      total_missed += 1
    

  print ("\n\nMEAN USER SCORE: " + str(user_mean) + " STDEV: " + str(user_stdev))
  print ("MEAN NON-USER SCORE: " + str(non_user_mean) + " STDEV: " + str(non_user_stdev))

  # run accuracy stats
  print("\n\n" + str((total_caught / total_users)*100) + "% of users detected.")
  print(str((total_caught / total_users - 1)*(-100)) + "% of users not detected.")
  print(str((total_false_pos / total_pos)*100) + "% of positive predictions were false positives.")
  print(str((total_users/total_predictions)*100) + "% of the sample were users.")

  pass

# calculates mean from set of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))

# calculates std deviation from set of numbers
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def calculateProbability(score, mean, stdev):
	exponent = math.exp(-(math.pow(score-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

