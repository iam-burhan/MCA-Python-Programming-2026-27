num = int(input("Enter a positive integer: "))

if num == 0:
    print("Number of digits: 1")
    print("Largest digit: 0")
    print("Smallest digit: 0")
else:
    temp = num
    count = 0
    largest = 0
    smallest = 9

    while temp > 0:
        digit = temp % 10
        count = count + 1
        
        if digit > largest:
            largest = digit
            
        if digit < smallest:
            smallest = digit
            
        temp = temp // 10

    print("Number of digits:", count)
    print("Largest digit:", largest)
    print("Smallest digit:", smallest)