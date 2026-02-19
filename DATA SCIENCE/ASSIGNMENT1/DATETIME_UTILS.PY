'''Create a Python module called datetime_utils.py that includes the following functions:
• get_current_time(): Returns the current time in "HH:MM:SS" format.
• get_current_date(): Returns the current date in "YYYY-MM-DD" format.
• days_between_dates(date1, date2): Takes two dates in the format "YYYY-MM-DD" and
returns the number of days between the two dates.'''
import datetime
def get_current_time():
    curtime=datetime.datetime.now().time()
    print("CURRENT TIME IS: ",curtime)
def get_current_date():
    currentdate=datetime.date.today()
    print("CURRENT DATE IS: ",currentdate)
def days_between_dates(date1, date2):
    Y1,Y2=int(date1[0:4]),int(date2[0:4])
    M1,M2=int(date1[5:7]),int(date2[5:7])
    D1,D2=int(date1[8:10]),int(date2[8:10])
    '''print(Y1,Y2)
    print(M1,M2)
    print(D1,D2)'''
    if Y1>Y2:
        if D1>=D2:
            DCNT=D1-D2
        else:
            DCNT=(30+D1)-D2
            M1-=1
        if M1>=M2:
            MDCNT=(M1-M2)*30
        else:
            MDCNT=(((M1+12))-M2)*30
            Y1-=1
        YDCNT=(Y1-Y2)*365
        print("TOTAL NUMBER OF DAYS BETWEEN GIVEN DATES:",DCNT+MDCNT+YDCNT)
    """elif Y1==Y2:
        if M1>M2:
            if D1>=D2:
                DCNT=D1-D2
            else:
                DCNT=(30+D1)-D2
                M1-=1
            MDCNT=(M1-M2)*30
            print("TOTAL NUMBER OF DAYS BETWEEN GIVEN DATES:",DCNT+MDCNT+YDCNT)"""
        


            
        



DATE1=input("ENTER DATE 1 IN YYYY-MM-DD FORMAT : ")
DATE2=input("ENTER DATE 2 IN YYYY-MM-DD FORMAT: ")
days_between_dates(DATE1,DATE2)
get_current_date()
get_current_time()
