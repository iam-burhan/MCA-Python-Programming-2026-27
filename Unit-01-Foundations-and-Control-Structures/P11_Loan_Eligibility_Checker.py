age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
if age >= 21 and income >= 25000 and credit_score >= 700:
    print("Eligible for Loan!")
else:
    print("Not Eligible for Loan.")