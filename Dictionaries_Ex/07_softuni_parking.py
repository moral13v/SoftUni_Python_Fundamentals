n = int(input())
parking = {}

for i in range(n):
    command_args = input().split()
    action = command_args[0]
    user = command_args[1]
    if action == "register":
        registration = command_args[2]
        if user not in parking:
            parking[user] = registration
            print(f"{user} registered {parking[user]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[user]}")
    elif action == "unregister":
        if user in parking:
            parking.pop(user)
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")

for user in parking:
    print(f"{user} => {parking[user]}")
