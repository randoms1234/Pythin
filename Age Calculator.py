import time
import datetime

now= datetime.datetime.now()
A=time.asctime()
print(A)
print(now.year)
day=input("What day were you born on?")
Month=input("What month were you born on?")
Year=input("What year were you born on?")
age=0

if len(day)==2:
    print(day)
    day=int(day)
    if len(Month)==2:
        print(Month)
        Month=int(Month)
        if len(Year)==4:
            print(Year)
            Year=int(Year)
           

        else:
            print("errr no")

    else:
        print("no")

else:
    print("why?")

age= 2016-Year
if Month < 6:
    age= age -1
    print(age)

elif Month > 6:
    age=age-1
    print(age)
