numbers = [65, 2000, 3, 99, 800, 21, 56, 11, 9, 812, 1500]

# Selection Sort
length = len(numbers)
for i in range(length-1):
    s = numbers[i]
    position = i
    for j in range(i+1, length):
        if numbers[j] < s:
            s = numbers[j]
            position = j
    temp = numbers[i]
    numbers[i] = numbers[position]
    numbers[position] = temp
    print(numbers)

# Bubble Sort

print("Bubble Sort:")

numbers = [65, 2000, 3, 99, 800, 21, 56, 11, 9, 812, 1500]

index = 0

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
print(numbers)

# Insertion Sort

print("Insertion Sort:")

numbers = [3065, 2000, 3, 99, 800, 21, 56, 11, 9, 812, 1500]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i-1
    while j >= 0 and key < numbers[j]:
        numbers[j+1] = numbers[j]
        j = j - 1
    numbers[j+1] = key

print(numbers)