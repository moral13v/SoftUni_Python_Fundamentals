version = int("".join(input().split("."))) + 1
next_version = list(str(version))
print(".".join(next_version))


# if version[-1] + 1 > 9:
#     version[-1] = 0
#     if version[1] + 1 > 9:
#         version[0] += 1
#         version[1] = 0
#     else:
#         version[1] += 1
# else:
#     version[-1] += 1
#
#
# print(f"{version[0]}.{version[1]}.{version[-1]}")


