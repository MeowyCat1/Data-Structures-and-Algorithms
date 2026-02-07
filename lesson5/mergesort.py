list = [5, 8, 9 , 1, 4, 3]

def mergesort(list, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(list, low, mid)
        mergesort(list, mid + 1, high)
        merge(list, low, mid, high)

def merge(list, low, mid, high):
    mergelist = []
    start1 = low
    start2 = mid + 1
    while start1 <= mid and start2 <= high:
        if list[start1] < list[start2]:
            mergelist.append(list[start1])
            start1 += 1
        else:
            mergelist.append(list[start2])
            start2 += 1
    while start1 <= mid:
        mergelist.append(list[start1])
    while start2 <= high:
        mergelist.append(list[start2])
    k = 0
    for i in range(low, high + 1):
        list[i] = mergelist[k]
        k += 1

mergesort(list, 0, 5)
print(list)