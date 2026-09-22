maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
total_marks = maths + physics + chemistry
overall_percentage = (total_marks / 300) * 100
if maths >= 50 and physics >= 50 and chemistry >= 50 and overall_percentage >= 60:
    print("Status: Eligible for Admission")
else:
    print("Status: Not Eligible for Admission")