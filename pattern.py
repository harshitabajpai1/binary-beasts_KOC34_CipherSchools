#print("SWOT ANALYSIS")
#print('domain name: web developer')
#print('name: Harshita Bajpai')
#print('section:KOC34')
#print('registration no.: 12217492')
#print('roll no.:RKOC34B48')


#pattern 1
def square(n):

    #n=int(input())
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n:
                print("*",end=' ')
            else:
                print(" ",end=" ")
        print("\r")

n=int(input())
square(n)         

#pattern 2
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print('\r')                
