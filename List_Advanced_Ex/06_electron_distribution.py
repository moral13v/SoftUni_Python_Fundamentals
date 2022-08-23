number_of_electrons = int(input())
shells = []

for i in range(1, number_of_electrons + 1):
    shell = 2 * (i ** 2)
    if number_of_electrons <= shell:
        shell = number_of_electrons
        shells.append(shell)
        break
    number_of_electrons -= shell
    shells.append(shell)


print(shells)
