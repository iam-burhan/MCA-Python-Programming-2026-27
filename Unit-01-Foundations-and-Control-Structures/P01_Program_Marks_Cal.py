marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")