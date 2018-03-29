class hashTable:
    def __init__(self,listSize):
        self.size=listSize
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def put(self,key,data):
        hashValue=self.hashFunction(key,len(self.slots))
        # print(hashValue,key)

        if self.slots[hashValue]==None:
            self.slots[hashValue]=key
            self.data[hashValue]=data
        else:
            if self.slots[hashValue]==key:
                self.data[hashValue]=data
            else:
                nextSlot=self.rehashFunc(hashValue,len(self.slots))
                while self.slots[nextSlot]!=None and self.slots[nextSlot]!=key:
                    nextSlot=self.rehashFunc(nextSlot,len(self.slots))

                    if self.slots==None:
                        self.slots[nextSlot]=key
                        self.data[nextSlot]=data
                    else:
                        self.data[nextSlot]=data
        # print(str(self.slots))

    def hashFunction(self,key,sizeOfSlots):
        return key%sizeOfSlots
    
    def rehashFunc(self,oldHash,sizeOfSlots):
        return (oldHash+1)%sizeOfSlots

    def getItem(self,key):
        startSlot=self.hashFunction(key,len(self.slots))
        data=None
        found=False
        stop=False
        currPosition=startSlot
        # print(str(self.slots),startSlot,currPosition)
        # print(self.slots[currPosition],found,stop)
        while self.slots[currPosition]!=None and found== False and stop ==False:
            # print(currPosition,found)
            if self.slots[currPosition]==key:
                found=True
                data=self.data[currPosition]
            else:
                currPosition=self.rehashFunc(currPosition,len(self.slots))
                if currPosition == startSlot:
                    stop=True
            
        # print(data)
        if data==None:
            return "No data found"
        else:
            return data

    def __getitem__(self,key):
        return self.getItem(key)

    def __setitem__(self,key,data):
        self.put(key,data)

h=hashTable(11)
h.put(54,'cat')
h.put(26,'dog')
h.put(93,'lion')
print(h.getItem(20))