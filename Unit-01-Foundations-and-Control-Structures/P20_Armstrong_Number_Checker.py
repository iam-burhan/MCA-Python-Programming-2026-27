num = int(input("Enter a positive integer: "))

str_num = str(num)
num_digits = len(str_num)

temp = num
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum = armstrong_sum + (digit ** num_digits)
    temp = temp // 10

if num == armstrong_sum:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is NOT an Armstrong Number.")