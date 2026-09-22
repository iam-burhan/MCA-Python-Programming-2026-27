num = int(input("Enter an integer: "))

factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print(f"Factors of {num}: {factors}")
print(f"Total number of factors: {len(factors)}")