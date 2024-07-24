# write a program to print all the prime numbers in a given range

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)    