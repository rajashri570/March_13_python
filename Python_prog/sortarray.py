#Write a Program to sort the array in ascending order .

import array as arr

n=5
num=arr.array('i',[])
for i in range(n):
	num.append(int(input(" Enter Value: ")))

temp = 0
small = num[0]
for i in range(len(num)) :
	for j in range(len(num)-i-1) :
		if num[j] > num[j+1]  :
			temp =  num[j]
			num[j] =num[j+1]
			num[j+1]=temp
for i in num:
	print(i ,end =' ')
print()
