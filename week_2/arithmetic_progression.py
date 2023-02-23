import math
#solving sum in arithmetic progression
n= int(input("enter n:"))
a = int(input("enter a:"))
d = int(input("enter d:"))

sn=(n/2)*(2*a + (n-1)*d)

print("the sum of the numbers is:",sn)


print("--------------------------------------------")

#solving sum in  geometric progression

a=int(input("enter a:"))
r=int(input("enter r:"))
n=int(input("enter n:"))
if(r>1):
    sn=(a*((r**n) - 1))/(r-1)
    print("the sum of the numbers is :",sn)
else:
    if(r<1):
        sn=(a*(1 - (r**n)))/(1-r)
    print("the sum of the numbers is :",sn)