print("STUDENT  GRADE SYSTEM")
name=input("Enter student name")
mark1=float(input("Enter your first mark"))
mark2=float(input("Enter your second mark"))
mark3=float(input("Enter your third mark"))
average=(mark1+mark2+mark3)/3
print("Student:",name)
print("average:",average)
if average>=90:
 print("Grade: A")
elif average >=75:
 print("Grade: B")
elif average >=60:
 print("Grade: C")
elif average >=50:
 print("Status: PASS")
else:
 print("Status: FAIL")
 
