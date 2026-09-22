n = int(input("Enter total number of students: "))

marks = []
print("Enter the marks of students one by one:")
for i in range(n):
    m = float(input(f"Enter mark for student {i + 1}: "))
    marks.append(m)

passed = 0
above_75 = 0

for m in marks:
    if m >= 40:
        passed = passed + 1
    if m > 75:
        above_75 = above_75 + 1

failed = n - passed

print("\n--- Summary ---")
print("Total Students:", n)
print("Passed Students (>= 40):", passed)
print("Failed Students (< 40):", failed)
print("Students with Distinction (> 75):", above_75)