class binaryTree:
    def __init__(self,element):
        self.key=element
        self.left=None
        self.right=None
        self.parent=None
    
    def insertLeft(self,newNode):
        if self.left==None:
            self.left=binaryTree(newNode)
        else:
            t=binaryTree(newNode)
            t.left=t
            t.parent=self.left
            self.left=t
    
    def insertRight(self,newNode):
        if self.right==None:
            self.right=binaryTree(newNode)
        else:
            t=binaryTree(newNode)
            t.right=self.right
            self.right=t
    
    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# r = binaryTree('1')
# print(r.getRootVal())
# r.insertLeft('2')
# print(r.getLeft().getRootVal())
# r.insertRight('3')
# print(r.getRight().getRootVal())
# r.getRight().setRootVal('hola')
# print(r.getRight().getRootVal())