'''h = eval(input("Enter diamond's height:"))

for x in range (h):
    print( " " * (h-x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print( " " * (h-x), "x" * (2*x + 1))'''
import cmath

first_coefficient = int(input("enter the first coefficient:"))
second_coefficient = int(input("enter the second coefficient"))
constant = int(input("enter the constant"))

ans1= -abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)
ans2= -abs(second_coefficient) + cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)

print("the answers are"+str(ans1)+" and "+str(ans2))

R = int(input("enter range:"))
#using for loop to draw a triangle
for diamond in range(R):
    print(" " * (R - diamond), "*" * (2 * diamond + 1))

print("------------------------------------------------")

#using for loop to draw pascals triangle
for i in range(1, R+1):
    for j in range(0, R-i+1):
        print(' ', end=' ')

        #first element is always 1
        c= 1
        for j in range(1, i + 1):

            #first value in a line is always 1
            print(' ', c, seps='', end='')

            #using binomial coefficient
            c=c * (i-j) // j
        print()


