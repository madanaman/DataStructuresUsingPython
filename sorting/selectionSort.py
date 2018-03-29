def replacePos(lst,strt,end):
    # print('pre replacement',lst)
    print('replacing',lst[strt],'with',lst[end])
    temp=lst[strt]
    lst[strt]=lst[end]
    lst[end]=temp
    # print('post replacement',lst)

def findMax(lst,endIdx):
    maxIdx=0
    maxValue=lst[maxIdx]
    # print(lst)
    # print('before loop',maxIdx,maxValue)
    for i in range(0,endIdx+1):
        # print('before iteration',i,'maxvalue',maxValue,'maxIdx',maxIdx,'end index ',endIdx)

        if i==0:
            # print('first loop')
            maxIdx=0
            maxValue=int(lst[maxIdx])
            continue
        else:
            # print('checking if ',maxValue,type(maxValue),'is greater than ',lst[i],type(lst[i]))
            if lst[i]>maxValue:
                # print('inside if')
                maxValue=lst[i]
                maxIdx=i
        # print('after iteration','maxvalue',maxValue,'maxIdx',maxIdx)
    return maxIdx

def selectionSort(lst):
    idxToProcess=len(lst)-1
    for i in range(0,len(lst)):
        # print('iteration',i,'idxToProcess',idxToProcess)
        idx=findMax(lst,idxToProcess)
        print('maximum value found at',idx)
        replacePos(lst,idxToProcess,idx)
        idxToProcess=idxToProcess-1
    return(lst)
lst=[1,3,0,2,-1]
# lst=[1,2,0,4,3]
# lst=[1,3,0,2]
print(lst)

# print(findMax(lst,3))
print('Sorted List:',selectionSort(lst))

# for i in range(0,10):
    # print(i)