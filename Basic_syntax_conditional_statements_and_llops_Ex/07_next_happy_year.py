current_year = int(input())+1
year_is_not_found = True

while year_is_not_found:
    year_is_happy = True
    cur_year_string = str(current_year)
    for index_1 in range(len(cur_year_string)):
        for index_2 in range(len(cur_year_string)):
            if index_1 == index_2:
                continue
            if cur_year_string[index_1] == cur_year_string[index_2]:
                year_is_happy = False
                break
    if year_is_happy:
        print(current_year)
        year_is_not_found = False
    else:
        current_year += 1



