gifts = input().split()

command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        command_args = command[1]
        for gift in gifts:
            if gift == command_args:
                index = gifts.index(gift)
                gifts.remove(gift)
                gifts.insert(index, "None")
    elif "Required" in command:
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    elif "JustInCase" in command:
        gifts.pop(len(gifts) - 1)
        gifts.append(command[1])
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
