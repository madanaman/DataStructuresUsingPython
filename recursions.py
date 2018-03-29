'''
Problem 1:Find out sum of the number in the list
'''
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
    if len(numList)==1:
       return int(numList[0])
    else:
        return int(numList[0])+listsum1(numList[1:])

print(listsum1(['1','2','3','4','5']))

'''
Problem 2: Reverse a string
'''
stringToReverse='Aman'
#Normal Approach
def stringRev1(ipString):
    finalString=''
    for i in range(len(ipString)-1,-1,-1):
        finalString=finalString+ipString[i]
    return finalString

print(stringRev1(stringToReverse))

#Recursion Approach
def stringRev2(ipString):
    if len(ipString)==1:
        return ipString[0]
    else:
        return stringRev2(ipString[1:])+ipString[0]

print(stringRev2(stringToReverse))

'''Print list of numbers of array'''
a=[1,2,3,4,5]
def arrayPrint(ip):
    # print(ip)
    # len(ip)
    if len(ip)==1:
        return (ip[0])
    if (len(ip)>1):
        print(ip[0])
        arrayPrint(ip[1:])

arrayPrint(a)
