num = int(input("Enter a positive integer: "))

temp = num
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp = temp // 10

if num == reversed_num:
    print(num, "is a Palindrome.")
else:
    print(num, "is NOT a Palindrome.")