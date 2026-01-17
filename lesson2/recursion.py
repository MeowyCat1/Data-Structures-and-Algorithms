def counting(num):
    count = 0
    while count != num:
        count += 1
        print(count)

counting(5)
counting(20)
counting(1)
counting(12)

def hello(num):
    if num == 0:
        return
    else:
        print("Hello World")
        return hello(num-1)

hello(10)

def recursivecount(n):
    if n == 0:
        return 0
    else:
        print(n)
        return recursivecount(n-1)
    
recursivecount(5)

def recursivesum(n):
    if n == 0:
        return 0
    else:
        return n+recursivesum(n-1)
sum = recursivesum(5)
print(sum)

def recursivemultiply(n):
    if n == 1:
        return 1
    else:
        return n * recursivemultiply(n-1)
    
multiply = recursivemultiply(4)
print(multiply)