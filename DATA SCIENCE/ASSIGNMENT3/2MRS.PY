D={'INCEPTION': 5, 'AVATAR': 4, 'TITANIC': 3}
print("THE MOVIES RECORDED IN THE SYSTEM ARE: ",D)
def CHE():
    print("SELECT FROM OPTIONS GIVEN BELOW: \n ENTER 1 TO ADD A NEW MOVIE TO SYSTEM. \n ENTER 2 TO UPDATE THE RATING OF AN EXISTING MOVIE. \n ENTER 3 TO REMOVE AN EXISTING MOVIE FROM SYSTEM. \n ENTER 4 TO FIND THE HIGHEST RATED MOVIE. \n ENTER 5 TO FIND THE AVERAGE RATING OF ALL THE MOVIES. ")
    A=int(input("ENTER YOUR CHOICE: "))
    
    if A==1:
        ADD_NM()
    elif A==2:
        UPD_MV()
    elif A==3:
        DEL_MV()
    elif A==4:
        HGH_RT()
    elif A==5:
        AVG_RTG()
    else:
        print("INVALID CHOICE.PLEASE TRY AGAIN.")
        CHE()
def ADD_NM():
    A=int(input("ENTER THE NUMBER OF MOVIES YOU WISH TO ADD TO SYSTEM: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE MOVIE: ")
        P=float(input("ENTER THE RATING OF THE MOVIE: "))
        D[K.upper()]=P
    print("THE MOVIES RECORDED IN THE SYSTEM ARE: ",D)
    CHE()
def UPD_MV():
    A=int(input("ENTER THE NUMBER OF MOVIES WHOSE RATING YOU WISH TO UPDATE: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE MOVIE WHOSE RATING IS TO BE UPDATED: ")
        NP=float(input("ENTER THE NEW RATING: "))
        D[K.upper()]=NP
    print("UPDATED RECORD OF MOVIES IS: ",D)
    CHE()
def DEL_MV():
    A=int(input("ENTER THE NUMBER OF MOVIES YOU WISH TO DELETE FROM THE SYSTEM: "))
    for i in range(0,A):
        K=input("ENTER THE NAME OF THE MOVIE WHICH IS TO BE REMOVED FROM THE SYSTEM: ")
        D.pop(K.upper())
    print("UPDATED RECORD OF MOVIES IS: ",D)
    CHE()
def HGH_RT():
    F=list(D.values())
    C=max(F)
    G=list(D.keys())
    H=[]
    for i in G:
        if D[i]==C:
            H.append(i)
    print("THE MOVIES WITH HIGHEST RATING ARE",H,"WITH A RATING OF",C)
    CHE()
def AVG_RTG():
    K=list(D.values())
    L=len(K)
    C=0
    for i in K:
        C+=i
    print("THE AVERAGE RATING OF ALL THE MOVIES IS: ",C/L)
    CHE()
CHE()
