n = int(input())
students = {}

for i in range(n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student in students:
    average_grade = sum(students[student]) / len(students[student])
    students[student] = average_grade

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

for student in sorted_students:
    if student[1] >= 4.50:
        print(f"{student[0]} -> {student[1]:.2f}")
