data = input()
company_users = {}

while data != "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)
    data = input()

sorted_companies = sorted(company_users.items(), key=lambda x: x[0])

for company_kvp in sorted_companies:
    print(company_kvp[0])
    for employee in company_kvp[1]:
        print(f"-- {employee}")
