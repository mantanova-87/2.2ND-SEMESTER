'''Write a Python program that: 
• Takes a list of integers (with possible duplicates) as input. 
• Converts the list into a set to remove duplicates and prints the resulting set. 
• Convert the set back into a sorted list and display the sorted list.
MANTAVYA KUMAR'''
LST=eval(input("ENTER A LIST OF INTEGERS SEPARAETD BY COMMA TO STORE IN A LIST: "))
SET=set(LST)
print("THE LIST CONVERTED TO SET TO REMOVE DUPLICATES IS: ",SET)
LIST=sorted((SET))
print("THE UNORDERED SET CONVERTED INTO SORTED LIST IS: ",LIST)