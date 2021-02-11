#!/usr/localbin/python3
# Make a function that converts the grade into concept.
# Take a float value as a input and receive a string value as a answer. For grades more than 10 or less than 0, it'll be print "Invalid grade"

# Concepts                       Grades
# A                            10 to 9.1
# A-                           9 to 8.1
# B                            8 to 7.1
# B-                           7 to 6.1
# C                            6 to 5.1
# C-                           5 to 4.1
# D                            4 to 3.1
# D-                           3 to 2.1
# E                            2 to 1.1
# E-                           1 to 0

def grade_concept(value):
    grade = float(value)

    if grade > 10:
        return "Invalid grade"
    elif grade >= 9.1:
        return "A"
    elif grade >= 8.1:
        return "A-"
    elif grade >= 7.1:
        return "B"
    elif grade >= 6.1:
        return "B-"
    elif grade >= 5.1:
        return "C" 
    elif grade >= 4.1:
        return "C-"
    elif grade >= 3.1:
        return "D"
    elif grade >= 2.1:
        return "D-"
    elif grade >= 1.1:
        return "E"
    elif grade >= 0:
        return "E-"
    else:
        return "Invalid grade"

if __name__ == '__main__':
    input=input('Student grade:')
    concept=grade_concept(input)
    print(concept)









