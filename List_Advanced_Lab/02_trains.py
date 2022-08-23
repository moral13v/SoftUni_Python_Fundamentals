train = [0 for wagon in range(int(input()))]
action = input().split()

while action[0] != "End":
    command = action[0]
    if command == "add":
        train[-1] += int(action[1])
    elif command == "insert":
        train[int(action[1])] += int(action[2])
    elif command == "leave":
        train[int(action[1])] -= int(action[2])
    action = input().split()

print(train)
