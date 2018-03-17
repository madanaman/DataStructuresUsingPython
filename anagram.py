def anagram(s1,s2):
    s2List = list(s2)
    anagramBool=False
    for i in list(s1):
        # print i
        posj = 0
        for j in s2List:
            if(i is not None and i==j):
                # print(i,j,posj)
                anagramBool=True
                s2List[posj]=None
                # print(s2List)
                posj=posj+1
                break
            else:
                anagramBool=False
                posj=posj+1
        # print(anagramBool)

    print(s1,s2,anagramBool)
        
                

anagram("roast beef","eat for BSE")