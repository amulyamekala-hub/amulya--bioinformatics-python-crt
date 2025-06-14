students = []
for i in range(1, 6):
    print(f"\nEnter marks for Student {i}:")
    marks = []
    for j in range(1, 4):
        mark = int(input(f"  Subject {j} marks: "))
        marks.append(mark)
    total = sum(marks)
    avg = total / 3
    if avg > 90:
        grade = "1st Class"
    elif avg > 75:
        grade = "2nd Class"
    elif avg > 50:
        grade = "3rd Class"
    else:
        grade = "Fail"
    students.append({
        "Student": f"Student {i}",
        "Marks": marks,
        "Total": total,
        "Average": avg,
        "Class": grade
    })
print("\n========== Student Report ==========")
for student in students:
    print(f"{student['Student']}: Marks = {student['Marks']}, Total = {student['Total']}, Avg = {student['Average']:.2f}, Class = {student['Class']}")
