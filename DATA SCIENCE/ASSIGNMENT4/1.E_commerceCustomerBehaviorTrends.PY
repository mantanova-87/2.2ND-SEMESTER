import numpy as np
import pandas as pd
np.random.seed(20)
NOSAM=200
CUSTOMER_ID=np.random.randint(0,201,size=NOSAM)
TIMEON_SITE=np.random.randint(60,300,size=NOSAM)
PAGES_VISITED=np.random.randint(1,10,size=NOSAM)
CART_ADDITIONS=np.random.randint(1,6,size=NOSAM)
PURCHASE_MADE=np.random.randint(0,6,size=NOSAM)
DEVICE_TYPE=np.random.choice(["Mobile","Desktop","Tablet"],size=NOSAM)
REFERRAL_SOURCE=np.random.choice(["Google","Facebook","Direct","Email"],size=NOSAM)
CUSTOMER_DATA=pd.DataFrame({"CUSTOMER_ID":CUSTOMER_ID,"TIMEON_SITE":TIMEON_SITE,"PAGES_VISITED":PAGES_VISITED,"CART_ADDITIONS":CART_ADDITIONS,"PURCHASE_MADE":PURCHASE_MADE,"DEVICE_TYPE":DEVICE_TYPE,"REFERRAL_SOURCE":REFERRAL_SOURCE})
print(CUSTOMER_DATA.head(NOSAM))
CUSTOMER_DATA.to_csv("CUSTOMER_DATA.csv", index=False)
df=pd.read_csv("CUSTOMER_DATA.csv")
print("FOLLOWING ARE THE CUSTOMERS WHO MADE A PURCHASE: ")
PURCHASE_FILTER=df[df["PURCHASE_MADE"]>0][["CUSTOMER_ID","PURCHASE_MADE"]]
print(PURCHASE_FILTER)
print("FOLLOWING ARE THE CUSTOMERS WHO MADE NO PURCHASE: ")
PURCHASE_FILTER2=df[df["PURCHASE_MADE"]==0][["CUSTOMER_ID","PURCHASE_MADE"]]
print(PURCHASE_FILTER2)
print("FOLLOWING ARE THE CUSTOMERS WHO ADDED ITEMS TO CART BUT  MADE NO PURCHASE: ")
PURCHASE_FILTER3=df[(df["PURCHASE_MADE"]==0) & (df["CART_ADDITIONS"]>0)][["CUSTOMER_ID","CART_ADDITIONS","PURCHASE_MADE"]]
print(PURCHASE_FILTER3)
counts=df["DEVICE_TYPE"].value_counts()
M=counts["Mobile"]
N=counts["Desktop"]
O=counts["Tablet"]
print("PERCENTAGE OF MOBILE DEVICE USED: ",((M*100)/200))
print("PERCENTAGE OF DESKTOP USE: ",((N*100)/200))
print("PERCENTAGE OF TABLET USED: ",((O*100)/200))
counts=df["REFERRAL_SOURCE"].value_counts()
print(counts)
D=dict(counts)
M=counts["Facebook"]
N=counts["Email"]
O=counts["Google"]
P=counts["Direct"]
L1=list(D.keys())
L2=[((M*100)/200),((N*100)/200),((O*100)/200),((P*100)/200)]
U=max(L2)
K=L2.index(U)
print("THE MOST USED REFERRAL SOURCE IS:",L1[K])