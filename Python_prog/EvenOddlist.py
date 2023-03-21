'''
Ass-3
1)Write a program to take array and create two list named as evenlist and oddlist from array.
2)write a recursive program to print the fibonacci series.
3)Write lambda function to convert given string to uppercase.
4)write a program to sort the array elements in ascending order.
5)Write a program to exchange the first and last letter of string.
'''
import array as arr
numarr = arr.array('i',[ 2,11,3,7,8,4 ])
evenList = []
oddList = []
for i in numarr :
	if i % 2 == 0 :
		evenList.append(i) 
	else :
		oddList.append(i)
print("Given Array is: ")
for i in numarr :
	print( i, end = " " )
print()
print("Even list :", evenList)
print("OddList is: ", oddList)
	
