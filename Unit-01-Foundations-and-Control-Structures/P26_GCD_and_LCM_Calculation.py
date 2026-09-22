a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

x, y = a, b
while y > 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print(f"GCD of {a} and {b} is: {gcd}")
print(f"LCM of {a} and {b} is: {lcm}")