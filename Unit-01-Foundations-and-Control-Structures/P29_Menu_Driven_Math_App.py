while True:
    print("\n--- Mathematical Application Menu ---")
    print("1. Check Prime Number")
    print("2. Check Palindrome Number")
    print("3. Check Armstrong Number")
    print("4. Calculate Factorial")
    print("5. Generate Fibonacci Series")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")

    if choice == '1':
        num = int(input("Enter number: "))
        if num <= 1:
            print(num, "is NOT a Prime Number.")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print(num, "is NOT a Prime Number.")
                    break
            else:
                print(num, "is a Prime Number.")

    elif choice == '2':
        num = int(input("Enter number: "))
        temp = num
        rev = 0
        while temp > 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp = temp // 10
            
        if num == rev:
            print(num, "is a Palindrome Number.")
        else:
            print(num, "is NOT a Palindrome Number.")

    elif choice == '3':
        num = int(input("Enter number: "))
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

    elif choice == '4':
        num = int(input("Enter number: "))
        if num < 0:
            print("Factorial does not exist for negative numbers.")
        elif num == 0:
            print("The factorial of 0 is 1.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial = factorial * i
            print("The factorial of", num, "is", factorial)

    elif choice == '5':
        terms = int(input("Enter number of terms: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        elif terms == 1:
            print("Fibonacci series: 0")
        else:
            a = 0
            b = 1
            print("Fibonacci series:", a, b, end=" ")
            for i in range(2, terms):
                c = a + b
                print(c, end=" ")
                a = b
                b = c
            print()

    elif choice == '6':
        print("Exiting application...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")