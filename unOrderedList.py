from Node import Node
class unOrderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def addItem(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head=temp
    
    def listSize(self):
        currentNode=self.head
        count=0
        while currentNode!=None:
            count=count+1
            currentNode=currentNode.getNext()
        return count
    
    def listSearch(self,item):
        currentNode=self.head
        itemFound=False
        while currentNode!= None and itemFound==False:
            # print(currentNode.getData(),item)
            if currentNode.getData()==item:
                itemFound=True
                break
            currentNode=currentNode.getNext()
        return itemFound
    
    def listRemove(self,item):
        currentNode = self.head
        previous = None
        itemFound = False

        while itemFound==False:
            if currentNode.getData()==item:
                itemFound=True
            else:
                previous=currentNode
                currentNode=currentNode.getNext()
            
        if previous == None:
            self.head=currentNode.getNext()
        else:
            previous.setNext(currentNode.getNext())
        
        
    
