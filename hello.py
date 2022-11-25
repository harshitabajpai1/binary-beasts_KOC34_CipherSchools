# p=float(input())  #have to write till 6  digits
#q=float(input())

#print('p='+str('%.6f'%p)+',q='+str('%.0f'%q)+',p+q='+str('%.2f'%(p+q))+',p-q='+str('%.2f'%(p-q)))

P=int(input())
R=3
T=2
if P>=1:
    SI=float(P*R*T)/100
    print(str('%.2f'%SI))
else:
    print('enter valid principal')    

