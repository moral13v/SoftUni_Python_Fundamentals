targets = [int(target) for target in input().split()]
command = input()

while command != "End":
    command_args = command.split()
    if command_args[0] == "Shoot":
        index = int(command_args[1])
        power = int(command_args[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command_args[0] == "Add":
        index = int(command_args[1])
        value = int(command_args[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command_args[0] == "Strike":
        index = int(command_args[1])
        radius = int(command_args[2])
        if index in range(len(targets))\
                and index + radius in range(len(targets))\
                and index - radius in range(len(targets)):
            for index in range(index - radius, index + radius + 1):
                targets[index] = 0
            targets = [target for target in targets if target != 0]
        else:
            print("Strike missed!")
    command = input()

targets = [str(target) for target in targets]
print("|".join(targets))
