""""" Exercises 9.1,9.2 and 9.3"""
#Angel Solis
#CIS129 Lab11
#05/02/2024

import csv
#Reminder: All of this was mande in ipython, however need somewhere to record and upload it
#Part 9.1
 with open('grades.txt', mode='w') as file:
     for grades in range(5):
         grade = input('Give your grades\n')
         file.write(f'{grade}\n')

#Part 9.2
with open('grades.txt', mode='r') as file:
    grades = file.readlines()
    grades = [int(grade.strip()) for grade in grades]
    average = sum(grades)/len(grades)
    print(f'The average found in grade text is {average}\
by count of {len(grades)} grades and a total of {sum(grades)}.')

#Part 9.3
#I expected another .txt ordered, not an excel.
with open('grades.csv', mode='a') as file:
    student_firstname = input("Student's first name: ")
    student_lastname = input("Student's last name: ")
    student_1grade = input("First exam grade: ")
    student_2grade = input("Second exam grade: ")
    student_3grade = input("Third exam grade: ")
    writer = csv.DictWriter(file, fieldnames=["firstname",
                                              "lastname",
                                              "exam1grade",
                                              "exam2grade",
                                              "exam3grade"])
    writer.writerow({"firstname": student_firstname,
                     "lastname": student_lastname,
                     "exam1grade":student_1grade,
                     "exam2grade":student_2grade,
                     "exam3grade":student_3grade})
