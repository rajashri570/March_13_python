#python program t find biggest number
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
if num1>num2:
	if num1%num2==0:
		print(f"{num1} is fully divisible by {num2}")
	else:
		print(f"{num2} does not divide {num1} completely")
else:
	if num2%num1==0:
		print(f"{num2} is fully divisible by {num1}")
	else:
		print(f"{num1} does not divide {num2} completely")

