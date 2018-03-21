from Dequeue import Dequeue

def palChecker(ipString):
    charDequeue = Dequeue()
    equalBool = True

    for ch in ipString:
        charDequeue.addRear(ch)
    
    charDequeue.printList()

    while charDequeue.size()>1 and equalBool==True:
        first = charDequeue.removeFront()
        last = charDequeue.removeRear()
        # print(first,last)

        if first!=last:
            equalBool = False
            break
    return equalBool

print(palChecker('aman'))
print(palChecker('ramar'))
        
