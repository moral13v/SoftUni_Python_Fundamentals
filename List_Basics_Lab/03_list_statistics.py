n = int(input())

positives = []
negatives = []

for i in range(n):
    number = int(input())
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
