from datetime import datetime
try:
    bday=input()
    day1=datetime.strptime(bday,'%d/%m/%Y').date()
    dday=input()
    day2=datetime.strptime(dday,'%d/%m/%Y').date()
    diff=(day2-day1)
    print("You lived",diff.days,"days")
except:
    print("You entered wrong date")
print('THANK YOU FOR USING OUR APP')         