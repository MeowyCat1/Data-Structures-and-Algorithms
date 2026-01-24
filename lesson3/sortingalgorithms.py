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