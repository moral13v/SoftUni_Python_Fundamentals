data = input()

students = {}

while ":" in data:
    student_name, student_id, course = data.split(":")
    #students[student_id] = [student_name, course]
    students.update({student_id: [student_name, course]})
    data = input()

for key in students.keys():
    if students[key][1] in data.replace("_", " "):
        print(f"{students[key][0]} - {key}")
