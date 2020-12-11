#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 7, Task 2
The “scores.csv” is a csv file exported from an Excel file. It has the scores 
for each student in three courses. It has the following content:

,Adrian Alice,Alexis Bruce,Braxton Conley,Bruce Lee,Cindy Kim
IS101,87,100,94,100,83
IS102,96,87,77,81,65
IS103,70,90,90,82,85

Use the DataFrame of Python’s pandas package to calculate and print the required output.

Calculate the grade for each student according to the following rules:
>= 90 A, >= 80 B, >= 70 C, >= 60 D, <60 F

Calculate the class GPA with two decimal places according to the following rule:
A 4.00, B 3.00, C 2.00, D 1.00, F 0.00

Print the GPA for each student and the whole class:
Adrian Alice 3.21
Alexis Bruce 2.74
Braxton Conley 2.32
…

The class GPA is 2.62
"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import pandas as pd
import csv

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants
READ_MODE = 'r'
DATA_FILE = 'scores.csv'

#########1#########2#########3#########4#########5#########6#########7#########8
# Functions
#--------1---------2---------3---------4---------5---------6---------7---------8#
def find_gp(raw_score):
    # Receive the raw score, convert to grade points, then return the result
    if raw_score >= 90:
        gp_score = 4.00
    elif raw_score >= 80:
        gp_score = 3.00
    elif raw_score >= 70:
        gp_score = 2.00
    elif raw_score >= 60:
        gp_score = 1.00
    else:
        gp_score = 0.00
        
    return gp_score

#########1#########2#########3#########4#########5#########6#########7#########8
# Main
#  Open and read the data file.  In this case, scores.csv
try:
    grades = pd.read_csv(DATA_FILE, delimiter=',', index_col=0, header=0)
except:
    print('The file \'scores.csv\' does not exist in the directory.')
    quit()  # Python threw an exception at this line.  Find solution.....

# Calculate the grade for each student
grade_points = grades.applymap(find_gp)

# Using grade_points, find the GPA of each student
GPAs = grade_points.mean().round(2)

# Calculate the class GPA with two decimal places
GPAs['The class GPA is'] = GPAs.mean().round(2)

# Print the GPA for each student and the whole class
print(GPAs.to_string())


# End of Main 