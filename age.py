def finding_maritalstatus(age):
	if age>=18:
		print("You Are Eligible for Marriage")
	if age<18:
		print("Your are not eligible for marriage")
	if age>=40:
		print("Your are too old and you are not eligible for marriage")
age=int(input("Enter Your Age:"))
print(finding_maritalstatus(age))