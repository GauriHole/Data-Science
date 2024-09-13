import math
student = {}
count = 0
num_stud = int(input("Enter number of student : "))
for i in range(num_stud):
    name = input("Enter Student's name : ")
    age = int(input("Enter Student's age : "))
    grade = float(input("Enter Student's Grade : "))
    student['name'] = name
    student['age'] = age
    student['grade'] = grade
    print(student)
    count=count+1

high_grade = -1
high_grade_stud = ""
for i in range(num_stud):
    if grade > high_grade:
        high_grade = grade
        high_grade_stud = name
print(f"The Student with Highest Grade is {high_grade_stud} with a grade of {high_grade}")

avg_age = (count + student['age'] )/ 5
print("Average age of Students : ",avg_age)
