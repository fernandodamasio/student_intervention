# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:20:29 2016

@author: ferna
"""

# Import libraries
import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import f1_score

# Read student data
student_data = pd.read_csv("student-data.csv")

# TODO: Calculate number of students
n_students = student_data.shape[0]

# TODO: Calculate number of features
n_features = student_data.shape[1] - 1

# TODO: Calculate passing students
n_passed = np.sum(np.in1d(student_data.passed, 'yes'))
print type(np.asscalar(n_passed))

# TODO: Calculate failing students
n_failed = n_students - n_passed

# TODO: Calculate graduation rate
grad_rate = n_passed / float(n_students)

# Print the results
print "Total number of students: {}".format(n_students)
print "Number of features: {}".format(n_features)
print "Number of students who passed: {}".format(n_passed)
print "Number of students who failed: {}".format(n_failed)
print "Graduation rate of the class: {}".format(grad_rate)
print "Graduation rate of the class: {:.2f}%".format(grad_rate)
