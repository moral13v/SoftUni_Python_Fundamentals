def load_bar(a):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    if a == 0:
        return bar
    for i in range(a // 10):
        bar[i] = "%"
    return bar


n = int(input())

if n == 100:
    print(f"{n}% Complete!")
    print(f"[{''.join(load_bar(n))}]")
else:
    print(f"{n}% [{''.join(load_bar(n))}]")
    print("Still loading...")



