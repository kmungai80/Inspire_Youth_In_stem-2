#write a program to print the factorial of a number using functions
def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-1)
        return fact_n
    
factorial(3)
print(factorial(3))


def simple_interest(p,r,t):
    simp=((p*r*t)/100)
    print(simp)


simple_interest(20000,10,2)

