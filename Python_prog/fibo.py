#WAP to print fibonacci series till a specific number

num1=0
num2=1
i=0
sum=0
print(i,end=' ')
while sum!=8:
	 sum=num1+num2
	 print(sum,end=' ')
	 num1=num2
	 num2=sum
	 i=i+1
print()
