num = int(input("Enter an integer: "))
if num > 0:
    pos_neg = "Positive"
elif num < 0:
    pos_neg = "Negative"
else:
    pos_neg = "Zero"

if num == 0:
    even_odd = "Neither Even nor Odd"
elif num % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

print(f"The number is {pos_neg} and {even_odd}.")