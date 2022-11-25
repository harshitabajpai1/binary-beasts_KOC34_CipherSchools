from datetime import datetime
bday=input()
day1=datetime.strptime(bday,'%d/%m/%Y').date()
dday=input()
day2=datetime.strptime(dday,'%d/%m/%Y').date()
diff=(day2-day1)

if diff.days>0:
    print("You lived",diff.days,"days")
else:
    print('you entered wrong dates ')

print('THANK YOU')      



