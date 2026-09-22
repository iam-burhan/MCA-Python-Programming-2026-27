num = int(input("Enter a positive integer: "))

if num <= 1:
    print(num, "is NOT a Prime Number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime Number.")
            break
    else:
        print(num, "is a Prime Number.")