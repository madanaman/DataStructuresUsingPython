class binaryTree1:
    def __init__(self, val):
        self.rootValue=val
        self.right=None
        self.left=None
        self.parent=None
    # Getter and setter methods
    def getRootValue(self):
        return self.rootValue
    
    def setRootValue(self,val):
        self.rootValue=val
    
    def addLeftNode(self,val):
        if self.left == None:
            # print('inside if',__name__)
            t=binaryTree1(val)
            t.parent=self
            self.left=t
        else:
            # print('inside else',__name__)
            t=binaryTree1(val)
            t.left=self.left
            t.parent=self
            self.left=t
    def addRightNode(self,val):
        if self.right==None:
            # print('inside if',__name__)
            t=binaryTree1(val)
            t.parent=self
            t.right=t
        else:
            t=binaryTree1(val)
            # print('inside else',__name__)
            t.right=self.right
            t.parent=self
            self.right=t
    
    def getRightNode(self):
        return self.right
    
    def getLeftNode(self):
        return self.left

rootNode=binaryTree1(2)
print(rootNode)
print(rootNode.getRootValue())
rootNode.addLeftNode(10)
print(rootNode.getLeftNode().getRootValue())
rootNode.addRightNode(30)
print(rootNode.getRightNode())