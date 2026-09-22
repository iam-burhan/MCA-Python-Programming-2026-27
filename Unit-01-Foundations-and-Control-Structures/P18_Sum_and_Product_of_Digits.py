num = int(input("Enter a positive integer: "))

temp = num
sum_digits = 0

if temp == 0:
    prod_digits = 0
else:
    prod_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    prod_digits = prod_digits * digit
    temp = temp // 10

print("Sum of digits:", sum_digits)
print("Product of digits:", prod_digits)