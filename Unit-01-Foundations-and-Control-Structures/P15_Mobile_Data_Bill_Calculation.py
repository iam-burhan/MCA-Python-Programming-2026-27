usage = float(input("Enter monthly data usage in GB: "))
bill = 0

if usage <= 10:
    bill = usage * 15
elif usage <= 30:
    bill = (10 * 15) + (usage - 10) * 12
else:
    bill = (10 * 15) + (20 * 12) + (usage - 30) * 10

print(f"Total Mobile Data Bill: ₹{bill:.2f}")