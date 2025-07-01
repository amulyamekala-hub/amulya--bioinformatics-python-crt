# 2. Write a python program to take n students details as input from the user including student name, student id, percentage and branch and note that you have to take the value of n input from the user
n = int(input("Enter the number of students: "))
for i in range(1, n + 1):
    print(f"Enter details for Student {i}:")
    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    percentage = float(input("Enter Percentage: "))
    branch = input("Enter Branch: ")