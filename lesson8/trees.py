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

mytree = Tree(5)
mytree.leftchild = Tree(11)
mytree.rightchild = Tree(16)
mytree.leftchild.leftchild = Tree(9)
mytree.leftchild.rightchild = Tree(6)
mytree.rightchild.leftchild = Tree(2)
mytree.rightchild.rightchild = Tree(4)

mytree.preorder()