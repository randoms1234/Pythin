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
    print("day:", day)
    day=int(day)
    if len(Month)==2:
        print("Month:", Month)
        Month=int(Month)
        if len(Year)==4:
            print("Year:", Year)
            Year=int(Year)
                

        else:
            print("errr no")

    else:
        print("no")

else:
    print("why?")
if Month > 1 and Month < 13:
    age= 2016-Year
    if day > 1 and day < 32:
        if Month < 6:
            age= age -1
            print("Your age is:", age)

        elif Month > 6:
            age=age-1
            print("Your age is:", age)
    else:
        easteregg=input("How many days are their in a month?")
        if len(easteregg)==2:
            easteregg=int(easteregg)
            if easteregg==30 or easteregg==31:
                print("You have some sense")
            else:
                print("Im done, GO!")
        else:
            print("How much dumber can you be? alot or alot?")
            
            
         
else:
    print("go back to maths")
