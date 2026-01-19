"""Write a Python program that takes two lists as input and: 
Converts them into sets. 
Computes and displays the union, intersection, and difference of these sets. 
Checks if one set is a subset or superset of the other. 
Finds the symmetric difference of the two sets. 
Output the results in a sorted manner.
MANTAVYA KUMAR,19-01-2026"""
L1=eval(input("ENTER A LIST OF INTEGERS SEPARATED BY COMMA TO STORE AS LIST 1: "))
L2=eval(input("ENTER A LIST OF INTEGERS SEPARATED BY COMMA TO STORE AS LIST 2: "))
L1=list(L1)
L2=list(L2)
print(type(L1),L1)
print(type(L2),L2)
SET1,SET2=set(L1),set(L2)
print("SET1: ",SET1)
print("SET2: ",SET2)
UNION=SET1.union(SET2)
INTERSECTION=SET1.intersection(SET2)
DIFFERENCE=SET1.difference(SET2)
print("THE UNION ,INTERSECTION AND DIFFERENCE OF THE SETS CREATED BY THE GIVEN LIST 1 AND LIST 2 ARE:\n ",UNION,",",INTERSECTION,"AND",DIFFERENCE,"RESPECTIVELY.")
A=SET1.issubset(SET2)
B=SET2.issubset(SET1)
C=SET1.issuperset(SET2)
D=SET2.issuperset(SET1)
if A==True:
    print("SET1 IS SUBSET OF SET2.")
else:
    print("SET1 IS NOT A SUBSET OF SET2.")
if B==True:
    print("SET2 IS SUBSET OF SET1.")
else:
    print("SET2 IS NOT A SUBSET OF SET1.")
if C==True:
    print("SET1 IS SUPERSET OF SET2.")
else:
    print("SET1 IS NOT A SUPERSET OF SET2.")
if D==True:
    print("SET2 IS SUPERSET OF SET1.")
else:
    print("SET 2 IS NOT SUPERSET OF SET1")
SD=SET1.symmetric_difference(SET2)
print("THE SYMMETRIC DIFFERENCE BETWEEN SET1 AND SET2 IS: ",SD)




