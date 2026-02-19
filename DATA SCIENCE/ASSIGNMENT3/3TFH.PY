'''Q3. Write a Python program that creates a file called students.txt and writes the following
information into it:
Name: Alice, Age: 22, Major: Computer Science
Name: Bob, Age: 24, Major: Mathematics
Name: Charlie, Age: 23, Major: Physics
Note: Add 10 instances.
i. Read from a file: Write a Python program to read the content from students.txt and
display it line by line.
ii. Count words in a file: Write a Python program that reads a text file and counts the
number of occurrences of each word in that file. Print the word frequency.
iii. Append to a file: Write a Python program that appends a new student's data (Name,
Age, and Major) to the students.txt file. Ensure the new data is written on a new
line.
iv. Copy file contents: Write a Python program to copy the contents of one file (e.g.,
source.txt) to another file (e.g., destination.txt).
v. File statistics: Write a Python program that accepts the name of a text file and displays
the following statistics:
o Number of lines in the file
o Number of words in the file
o Number of characters in the file'''
A=open("students.txt",mode="a+")
N=int(input("ENTER THE NUMBER OF LINES YOU WISH TO ENTER: "))
for i in range(1,N+1):
    print("ENTER LINE NO.",i,": ")
    S=input()
    A.write(S+'\n')
A.seek(0)
CF=A.readlines()
print(CF)
B=open("DESTINATION.txt","a")
for m in CF:
    B.write(m)

STR=""
for k in CF:
    STR=STR+k
print(STR)
D=STR.split()
j=len(D)
print(j)
for i in D:
    j+=len(i)
SEP=[":"," ",",","\n"]
for c in SEP:
    STR=STR.replace(c," ")
LST=STR.split()
print(LST)
L=[a.upper() for a in LST]
T=[]
for i in L:
    if i not in T:
        S=L.count(i)
        print("THE OCCURENCE OF WORD",i,"IN THE ENTERED SENTENCE IS",S)
        T.append(i)

print("TOTAL NUMBER OF LINES IN THE TEXT FILE IS: ",len(CF))
print("TOTAL NUNBER OF WORDS IN THE FILE IS: ",len(LST))
print("TOTAL NUMBER OF CHARACTERS IN THE FILE IS: ",j)
    



