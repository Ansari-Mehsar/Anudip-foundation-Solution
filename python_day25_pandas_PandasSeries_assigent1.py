#1: Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject.
#   You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.

import pandas as pd

# Input data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Creating a Pandas Series
scores_series = pd.Series(exam_scores, index=students, name="students scores")

# printing the Series
print(scores_series)

#output
"""
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      85
Hannah     89
Ivy        78
Jack       91
Name: students scores, dtype: int64

"""

