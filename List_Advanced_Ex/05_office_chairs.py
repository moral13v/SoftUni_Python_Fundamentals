n = int(input())
total_chairs = 0
total_visitors = 0
enough_chairs = True

for i in range(1, n + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        enough_chairs = False
        continue
    total_chairs += chairs
    total_visitors += visitors

if enough_chairs:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
