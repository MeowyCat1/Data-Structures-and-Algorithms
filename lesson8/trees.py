class Tree():
    def __init__(self, data, leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

    def inorder(self):
        if self.leftchild != None:
            self.leftchild.inorder()
        
        print(self.data)
        
        if self.rightchild != None:
            self.rightchild.inorder()

    def preorder(self):
        print(self.data)

        if self.leftchild != None:
            self.leftchild.preorder()
        
        
        if self.rightchild != None:
            self.rightchild.preorder()
    
    def postorder(self):
        if self.leftchild != None:
            self.leftchild.postorder()
        
        
        if self.rightchild != None:
            self.rightchild.postorder()

        print(self.data)

    def count(self):
        number = 1
        if self.leftchild != None:
            number += self.leftchild.count()
        if self.rightchild != None:
            number += self.rightchild.count()
        return number
    
    def getmax(self):
        if self.leftchild == None:
            left = 0
        else:
            left = self.leftchild.getmax()

        if self.rightchild == None:
            right = 0
        else:
            right = self.rightchild.getmax()

        if self.data == None:
            return 0
        else:
            return max(self.data, left, right)
        
    def search(self, number):
        if self.data == number:
            return True
        elif self.data > number and self.leftchild != None:
            return self.leftchild.search(number)
        elif self.data < number and self.rightchild != None:
            return self.rightchild.search(number)
        else:
            return False
        
    def insert(self, number):
        if self.data == number:
            print("Cannot add to tree, number already in tree.")
        elif number > self.data:
            if self.rightchild != None:
                self.rightchild.insert(number)
            else:
                self.rightchild = Tree(number)
        elif number < self.data:
            if self.leftchild != None:
                self.leftchild.insert(number)
            else:
                self.leftchild = Tree(number)



mytree = Tree(5)
mytree.leftchild = Tree(2)
mytree.rightchild = Tree(11)
mytree.leftchild.leftchild = Tree(1)
mytree.leftchild.rightchild = Tree(4)
mytree.rightchild.leftchild = Tree(9)
mytree.rightchild.rightchild = Tree(16)

mytree.preorder()
print("----Post Order----")
mytree.postorder()
print(f"Count: {mytree.count()}")
print(f"Max: {mytree.getmax()}")

numtofind = int(input("What number do you want to search for?: "))
print(f"found: {mytree.search(numtofind)}")

numtoadd = int(input("What number do you want to add?: "))
mytree.insert(numtoadd)
mytree.preorder()