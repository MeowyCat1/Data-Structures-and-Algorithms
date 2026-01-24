names = ["Bob", "Anna", "Sam"]

# Linear Search
inputname = input("Enter a name to search: ")
for name in names:
    if name == inputname:
        print("Found name!")

inputname = input("Enter a name to search: ")
if inputname in names:
    print("Found name!")

# Binary search
nums = [4, 8, 34, 68, 102, 155, 156, 192, 203, 5000]

first = 0
last = 9

found = False
inputnum = int(input("Enter a number to search: "))
while first <= last:
    middle = (first + last) // 2
    if nums[middle] == inputnum:
        found = True
        break
    elif inputnum > nums[middle]:
        first = middle + 1
    else:
        last = middle - 1
if found == True:
    print("Found it!")
else:
    print("Not found.")