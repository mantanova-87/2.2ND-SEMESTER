""" Write a Python program that asks the user for their age and prints:
"You are a child" if the age is less than 13,
 "You are a teenager" if the age is between 13 and 19,
"You are an adult" if the age is 20 or older"""
AGE=int(input("ENTER YOUR AGE: "))
if AGE<13:
    print("YOU ARE A CHILD.")
elif AGE>=13 and AGE<=19:
    print("YOU ARE ATEENAGER.")
else:
    print("YOU ARE AN ADULT.")