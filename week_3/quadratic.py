import math

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

sn1= (-b + math.sqrt((b**2- (4*a*c))))/2*a
sn2= (-b - math.sqrt((b**2- (4*a*c))))/2*a

print("first answer is :",sn1)
print("second answer is :",sn2)