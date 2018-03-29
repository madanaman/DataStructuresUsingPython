def insertionSort(lst):
    for index in range(1,len(lst)):

     currentvalue = lst[index]
     position = index

     while position>0 and lst[position-1]>currentvalue:
         lst[position]=lst[position-1]
         position = position-1

     lst[position]=currentvalue
    return lst

lst=[1,0,6,-1,-3,5]
print(insertionSort(lst))