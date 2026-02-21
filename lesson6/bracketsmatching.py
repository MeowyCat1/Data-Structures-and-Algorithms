from stacks import Stack

bracketstack = Stack(20)

opening = ["(", "[", "{"]

closing = [")", "]", "}"]

expression = input("Please may I have an expression?")

flag = False
for item in expression:
    print(bracketstack.display())
    if item in opening:
        bracketstack.push(item)
    elif item in closing:
        bracketindex = closing.index(item)
        if bracketstack.hasitem() and opening[bracketindex] == bracketstack.peek():
            bracketstack.pop()
        else:
            flag = True
            break
print(bracketstack.display())
if bracketstack.hasitem():
    flag = True

if flag == False:
    print("Expression Valid!")
else:
    print("Expression not Valid!")