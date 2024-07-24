# write a program for prime number or not

a=int(input("enter a number:"))
r=a*0.5
c=0
if a==1:
    print("not a prime")
elif a==2:
    print("prime")    
for i in range(2,int(r+1)):
    if a%i==0:
        c+=1
        break
if(c==0):
    print("prime")
else:
    print("not prime")
