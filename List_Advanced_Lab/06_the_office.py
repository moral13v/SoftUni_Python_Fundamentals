employees = input().split()
happiness_factor = int(input())

# employees = list(map(lambda x: int(x) * happiness_factor, employees))
# filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

employees = [int(employee) * happiness_factor for employee in employees]
filtered = [x for x in employees if x >= (sum(employees) / len(employees))]

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
