def perfect_number(a):
    aliquot_sum = 0
    for i in range(1, a):
        if a % i == 0:
            aliquot_sum += i
    if aliquot_sum == a:
        return True


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


