def mergeSort(inpList):
    print("Splitting ",inpList)
    if len(inpList)>1:
        mid = len(inpList)//2
        lefthalf = inpList[:mid]
        righthalf = inpList[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                inpList[k]=lefthalf[i]
                i=i+1
            else:
                inpList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            inpList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            inpList[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",inpList)

inpList = [54,26,93,17,77,31,44,55,20]
mergeSort(inpList)
print(inpList)