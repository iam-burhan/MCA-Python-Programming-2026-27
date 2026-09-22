units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 300 + (units - 100) * 5
elif units <= 300:
    bill = 800 + (units - 200) * 7
else:
    bill = 1500 + (units - 300) * 10

print("Total Electricity Bill: ₹", bill)