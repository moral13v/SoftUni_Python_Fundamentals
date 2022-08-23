data = input()
courses = {}

while data != "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    data = input()

sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

for course in sorted_courses:
    print(f"{course[0]}: {len(course[1])}")
    sorted_students = sorted(course[1])
    for student in sorted_students:
        print(f"-- {student}")


