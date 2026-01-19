'''Write a Python program that: 
Takes a list of strings as input (some strings may repeat). 
Creates a set from the list to remove duplicates. 
Then, for each unique string, counts its occurrences in the original list and displays the count. 
'''
A=input("ENTER THE STRINGS SEPARATED BY COMMAS TO STORE IN THE LIST: ")
LIST=A.split(",")
SET=set(LIST)
for i in SET:
    C=0
    for k in LIST:
        if i==k:
            C+=1
    print("THE OCCURENCE OF",i,"IN THE LIST IS: ",C)
