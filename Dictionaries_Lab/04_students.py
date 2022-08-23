data = input()

students = {}
courses = {}

while ":" in data:
    command_args = data.split(":")
    student_name = command_args[0]
    student_id = command_args[1]
    course = command_args[2]

    students[student_id] = student_name
    courses[student_id] = course

    data = input()


for key in courses.keys():
    if courses[key] in data.replace("_", " "):
        print(f"{students[key]} - {key}")


