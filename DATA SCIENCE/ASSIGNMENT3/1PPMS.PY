D={'APPLE': 1.5, 'BANANA': 0.9, 'WALNUT': 1.2}
print("PRODUCTS RECORDED IN SYSTEM ARE: ",D)
def CHE():
    print("SELECT FROM OPTIONS GIVEN BELOW: \n ENTER 1 TO ADD A NEW PRODUCT. \n ENTER 2 TO UPDATE THE PRICE OF AN EXISTING PRODUCT. \n ENTER 3 TO REMOVE AN EXISTING PRODUCT. \n ENTER 4 TO CALCULATE TOTAL PRICE OF ALL PRODUCTS. \n ENTER 5 TO UPDATE PRICE OF ALL PRODUCTS AFTER APPLYING A DISCOUNT. ")
    A=int(input("ENTER YOUR CHOICE: "))
    if A==1:
        ADD_NP()
    elif A==2:
        UPD_PRC()
    elif A==3:
        DEL_PR()
    elif A==4:
        TOT_PRC()
    elif A==5:
        DISC_PRC()
    else:
        print("INVALID CHOICE.PLEASE TRY AGAIN.")
        CHE()
def ADD_NP():
    A=int(input("ENTER THE NUMBER OF PRODUCTS YOU WISH TO ADD: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE PRODUCT: ")
        P=float(input("ENTER THE PRICE OF THE PRODUCT: "))
        D[K.upper()]=P
    print("THE PRODUCTS ARE: ",D)
    CHE()
def UPD_PRC():
    A=int(input("ENTER THE NUMBER OF PRODUCTS WHOSE PRICE YOU WISH TO UPDATE: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE PRODUCT WHOSE PRICE IS TO BE UPDATED: ")
        NP=float(input("ENTER THE NEW PRICE: "))
        D[K.upper()]=NP
    print("PRODUCTS RECORDED IN SYSTEM ARE: ",D)
    CHE()
def DEL_PR():
    A=int(input("ENTER THE NUMBER OF PRODUCTS YOU WISH TO DELETE: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE PRODUCT WHICH IS TO BE REMOVED: ")
        D.pop(K.upper())
    print("PRODUCTS RECORDED IN SYSTEM ARE: ",D)
    CHE()
def TOT_PRC():
    F=list(D.values())
    C=0
    for i in F:
        C+=i
    print("PRODUCTS RECORDED IN SYSTEM ARE: ",D)
    print("TOTAL PRICE OF ALL THE PRODUCTS IS Rs.",C)
    CHE()
def DISC_PRC():
    A=float(input("ENTER THE PERCENTAGE OF DISCOUNT TO APPLY ON ALL PRODUCTS: "))
    K=list(D.keys())
    for i in K:
        P=D[i]
        D[i]=P-((P*A)/100)
        print("THE UPDATED PRICE OF",i,"IS",D[i])
    print("PRODUCTS RECORDED IN SYSTEM ARE: ",D)
    CHE()
CHE()



    


