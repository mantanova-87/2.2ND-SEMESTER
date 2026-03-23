'''Write a function is_anagram(str1, str2) that checks whether two strings are anagrams of each 
other. The function should ignore spaces and be case-insensitive.'''
def is_anagram(A,B):
    C=A.upper()
    D=B.upper()
    L1=[]
    L2=[]
    for k in C:
        L1.append(k)
    for i in D:
        L2.append(i)
    C=0
    for k in L1:
        if k not in L2:
            C+=1
        elif k in L2:
            C1=L1.count(k)
            C2=L2.count(k)
            if C1==C2:
                C+=0
            else:
                C+=1
    if C==0:
        print("True")
    else:
        print("False")
S1=input("ENTER THE FIRST STRING: ")
S2=input("ENTER THE SECOND STRING: ")
is_anagram(S1,S2)

