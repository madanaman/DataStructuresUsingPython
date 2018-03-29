def replacePos(lst,strt,end):
    temp=lst[strt]
    lst[strt]=lst[end]
    lst[end]=temp

ipList=[3,4,10,6,5,11,1]
initialState=ipList.copy()


def bubbleSort(ipList):
    for j in range(1,len(ipList)):
        print("iteration",j)
        previous=0
        for i in range(0,len(ipList)):
            if i==0: print('\tinside bubble sort now')
            if i==0:
                previous=0
                continue
            else:
                if ipList[previous]>ipList[i]:
                    replacePos(ipList,previous,i)
            previous=i
            print('\t',ipList)
    return ipList

finalState=bubbleSort(ipList)
print('Unsorted List',initialState)
print('sorted list',finalState)
