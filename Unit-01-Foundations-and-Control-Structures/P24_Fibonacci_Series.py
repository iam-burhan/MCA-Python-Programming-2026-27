
n = int(input("How many terms? "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    print(a, end=" ")
    print(b, end=" ")
    
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c