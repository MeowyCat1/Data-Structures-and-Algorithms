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


mytree = Tree(5)
mytree.leftchild = Tree(11)
mytree.rightchild = Tree(16)
mytree.leftchild.leftchild = Tree(9)
mytree.leftchild.rightchild = Tree(6)
mytree.rightchild.leftchild = Tree(2)
mytree.rightchild.rightchild = Tree(4)

mytree.preorder()
print("----Post Order----")
mytree.postorder()
print(f"Count: {mytree.count()}")
print(f"Max: {mytree.getmax()}")