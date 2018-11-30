from Student import Student
import Classifier
import csv
import random
import math
import operator

students = []

# reads data from CleanedSurvey.csv
def read_data():

  with open("CleanedSurvey.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            print('Column names are  ' + ", ".join(row))
        elif line_count < 10000:
          # handle survey 
          for i in range(0,len(row)):
            if row[i] == '':
              row[i] = '-1'
          this_student = Student(row)
          students.append(this_student)
          # print(row)
        line_count += 1
  pass

def analyze_data():
  num_students = len(students)
  opiate_users = 0
  avg_opiate_score = 0
  avg_user_score = 0
  for i in range (0, num_students):
    student = students[i]
    avg_opiate_score += student.opiate_risk_score

    if student.opiate_use == 2:
      opiate_users += 1
      avg_user_score += student.opiate_risk_score

  print("STUDENTS: " + str(num_students) + ", USERS: " + str(opiate_users))
  print("AVG SCORE: " + str(avg_opiate_score/num_students) + ", OF USERS: " + str(avg_user_score/opiate_users))

  Classifier.knn_controller(students)

def main():
  read_data()
  analyze_data()
  pass
