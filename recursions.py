'''
Normal approach
'''
def listSum(numList):
    finalSum = 0
    for i in numList:
        finalSum = finalSum+int(i)
    return finalSum

print(listSum(['1','2','3','4','5']))

'''
Recursive approach
'''


def listsum1(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum1(numList[1:])

print(listsum1(['1','2','3','4','5']))