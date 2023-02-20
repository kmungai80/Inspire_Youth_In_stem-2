#write a program to calculayte 16%tax
#ranging between 100k -150k

#19%tax income between 150k -300k
#30%tax income is above 300k
#5%tax income is below 




net_income=200000


#150k
if(net_income>150000) & (net_income < 300000):
    gross_income=net_income + ((19/100)*net_income)
    print("net income is {} your gross income {}".format(net_income,gross_income))



gross_income=int(input("enter your gross income"))

#above 300k
if(gross_income >=300000):
    net_income=gross_income-((30/100)*gross_income)
    print("if your gross income is:{} your net income is {}".format(gross_income,int(net_income)))



#150k to less than 300k

gross_income=int(input("enter yor gross income"))

if(gross_income > 150000) & (gross_income < 300000):
    net_income=gross_income-((19/100)*gross_income)
    print("your gross income is {} and your net income is {}:".format(gross_income,net_income))


gross_income=int(input("enter your gross income"))
tax_group_a = gross_income * 0.05
tax_group_b = gross_income * 0.16
tax_group_c = gross_income * 0.19
tax_group_d = gross_income * 0.30

if(gross_income <=100000):
    print("gross income:",gross_income)
    print("net income:",gross_income-tax_group_a)

elif(gross_income > 100000) & (gross_income < 150000):
    print("gross income:",gross_income)
    print("net income:",gross_income-tax_group_b)

elif(gross_income >= 150001) & (gross_income <=300000):
    print("gross income:",gross_income)
    print("net income:",gross_income-tax_group_c)
 
else:
    print("gross income",gross_income)
    print("net income",gross_income-tax_group_d)
