a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
    if a == b == c:
        print("Classification: Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Classification: Isosceles Triangle")
    else:
        print("Classification: Scalene Triangle")
else:
    print("Invalid Triangle! Sum of any two sides must be greater than the third side.")