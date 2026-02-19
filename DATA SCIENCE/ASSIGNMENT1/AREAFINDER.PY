#Create a Python module that includes the following functions:  
# A function to calculate the area of a circle (given the radius).  
# A function to calculate the area of a rectangle (given length and width).  
# A function to calculate the area of a triangle (given base and height). 
def AROC():
    import math as M
    A=float(input("ENTER THE RADIUS OF CIRCLE TO CALCULATE ITS AREA: "))
    U=input("ENTER THE UNIT OF RADIUS: ")
    AREA=M.pi*A*A
    print("AREA OF THE CIRCLE IS",AREA,"SQUARE",U)
def AOR():
    L=float(input("ENTER THE LENGTH OF RECTANGLE IN METRES: "))
    B=float(input("ENTER THE BREADTH OF RECTANGLE IN METRES: "))
    ARR=L*B
    print("AREA OF RECTANGLE IS",ARR,"SQUARE METRES.")
def AOT():
    H=float(input("ENTER THE HEIGHT OF TRIANGLE IN METRES: "))
    B=float(input("ENTER THE BASE OF TRIANGLE IN METRES: "))
    AOTR=(1/2)*B*H
    print("AREA OF TRIANGLE IS",AOTR,"SQUARE METRES.")