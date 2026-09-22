percentage = float(input("Enter percentage: "))
if 0 <= percentage <= 100:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"
    print(f"Grade: {grade}")
else:
    print("Invalid Input! Percentage must be between 0 and 100.")