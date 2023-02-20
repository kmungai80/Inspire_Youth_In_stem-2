numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

sum_num = 0
for number in numbers:
    number = int(input("enter the number:"))
    sum_num = sum_num + number


avg_num = sum_num/10
print("the average number is :", avg_num)
