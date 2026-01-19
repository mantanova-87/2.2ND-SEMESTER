''' Write a Python function that accepts two list with integer elements. Now design function code to 
perform union between these two lists and store the result in third list and print .  '''
def SET_UNION():
    L1=eval(input("ENTER A LIST OF INTEGERS SEPARATED BY COMMA TO STORE AS LIST 1: "))
    L2=eval(input("ENTER A LIST OF INTEGERS SEPARATED BY COMMA TO STORE AS LIST 2: "))
    L1=list(L1)
    L2=list(L2)
    L3=L1+L2
    L4=[]
    print(L3)
    for k in L3:
        if k not in L4:
            L4.append(k)
    print("THE UNION OF THE ENTERED LISTS IS: ",L4)
SET_UNION()
