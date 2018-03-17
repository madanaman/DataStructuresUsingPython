''' 
This is code to find if a given strings are anagram are not .

'''
import time
import re
def anagram(s1,s2):
    start = time.clock()
    s2List = list(s2)
    is_anagram=False
    for i in list(s1):
        # print i
        posj = 0
        for j in s2List:
            if(i is not None and i==j):
                # print(i,j,posj)
                is_anagram=True
                s2List[posj]=None
                # print(s2List)
                posj=posj+1
                break
            else:
                is_anagram=False
                posj=posj+1
        # print(is_anagram)
    stop = time.clock()
    print(s1,s2,is_anagram,start,stop,stop-start)
        
def anagram_sort_and_compare(s1,s2):
    start = time.clock()
    is_anagram = True
    # print (s1,s2)
    s1_list = list(re.sub(' ','',s1).lower())
    s2_list = list(re.sub(' ','',s2).lower())
    s1_list.sort()
    s2_list.sort()
    # print (len(s1_list), len(s2_list))
    if len(s1_list)!=len(s2_list):
        print("lists are unequal. Hence are not anagram")
        return False
    for i in range(0,len(s1_list)-1):
        if s1_list[i] != s2_list[i]:
            print(s1_list[i],s2_list[i])
            is_anagram=False
            break
    stop=time.clock()
    print(s1,s2,is_anagram,start,stop,stop-start)

def anagram_using_count(s1_ip,s2_ip):
    start = time.clock()
    is_anagram = True
    s1=re.sub(" ",'',s1_ip)
    s2=re.sub(' ','',s2_ip)
    s1_dict = {}
    s2_dict = {}
    for i in s1.lower():
        if i in s1_dict:
            s1_dict[i]=s1_dict.get(i,0)+1
        else:
            s1_dict[i]=1
    for i in s2.lower():
        if i in s2_dict:
            s2_dict[i]=s2_dict.get(i,0)+1
        else:
            s2_dict[i]=1
    if len(s1_dict.keys())!=len(s2_dict):
        print("Number of elemnts are not same. Hence not anagram")
        return False

    for i in s1_dict:
        if s1_dict[i]!=s2_dict[i]:
            is_anagram=False
            break

    stop=time.clock()
    print(s1_ip,s2_ip,is_anagram,start,stop,stop-start)
        
anagram("roast beef","eat for BSE")
anagram_sort_and_compare("roast beef","eat for BSE")
anagram_using_count("roast beef","eat for BSE")