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
    d1=datetime.datetime(Y1,M1,D1)
    d2=datetime.datetime(Y2,M2,D2)
    difference = abs((d2 - d1).days)
    print("Number of days between the given dates is:", difference)

            
        




