start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

total_primes = 0

print("Prime numbers:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            total_primes = total_primes + 1

print("\nTotal prime numbers found:", total_primes)