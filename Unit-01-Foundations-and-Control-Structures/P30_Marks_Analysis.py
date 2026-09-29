
n = int(input("Enter number of students: "))
marks = []

for i in range(1, n + 1):
    m = float(input(f"Enter marks for student {i}: "))
    marks.append(m)

avg_marks = sum(marks) / n
highest = max(marks)
lowest = min(marks)

passed = sum(1 for m in marks if m >= 40)
failed = n - passed
above_75 = sum(1 for m in marks if m > 75)

print(f"\nClass Average: {avg_marks:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}")
print(f"Students Scoring > 75%: {above_75}")
