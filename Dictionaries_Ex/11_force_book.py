data = input()
force_book = {}

while data != "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in force_book:
            force_book[force_side] = []
        if force_user not in force_book[force_side]:
            force_book[force_side].append(force_user)

    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        for key, values in force_book.items():
            if force_user in values and key != force_side:
                values.remove(force_user)
        if force_side not in force_book:
            force_book[force_side] = []
        if force_user not in force_book[force_side]:
            force_book[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    data = input()

sorted_force_book = sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0]))

for kvp in sorted_force_book:
    if len(kvp[1]) > 0:
        print(f"Side: {kvp[0]}, Members: {len(kvp[1])}")
        sorted_users = sorted(kvp[1])
        for username in sorted_users:
            print(f"! {username}")



