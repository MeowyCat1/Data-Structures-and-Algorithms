class Stack():
    def __init__(self, n):
        self.n = n
        self.list = []
    def push(self, item):
        if len(self.list) < self.n:
            self.list.append(item)
        else:
            print("Stack is full")
    
    def pop(self):
        if len(self.list) > 0:
            self.list.pop()
        else:
            print("No items in stack, cannot remove.")
    
    def peek(self):
        if self.n > 0:
            return self.list[-1]
        else:
            print("No items in stack, cannot peek.")
    
    def display(self):
        return self.list
    
    def hasitem(self):
        if len(self.list) > 0:
            return True
        else:
            return False


mystack = Stack(5)

mystack.push("hello")
mystack.push("goodbye")
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.push("fjnfren")
mystack.push("fjnfren")
mystack.push("fjnfren")
mystack.push("fjnfren")
mystack.push("fjnfren")

print(mystack.display())