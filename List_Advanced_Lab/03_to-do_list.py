task = input()
to_do_list = [0] * 10

while task != "End":
    task_args = task.split("-")
    task_priority = int(task_args[0]) - 1
    task_content = task_args[1]
    # to_do_list.pop(task_priority)
    # to_do_list.insert(task_priority, task_content)
    to_do_list[task_priority] = task_content

    task = input()

result = [x for x in to_do_list if x != 0]
print(result)
