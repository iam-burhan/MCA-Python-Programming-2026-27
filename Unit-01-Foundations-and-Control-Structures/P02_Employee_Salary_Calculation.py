basic_salary = float(input("Enter Basic Salary: "))

da = 0.40 * basic_salary
hra = 0.20 * basic_salary
gross_salary = basic_salary + da + hra
tax = 0.10 * gross_salary
net_salary = gross_salary - tax

print(f"DA: {da:.2f}")
print(f"HRA: {hra:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
print(f"Tax Deduction: {tax:.2f}")
print(f"Net Salary: {net_salary:.2f}")