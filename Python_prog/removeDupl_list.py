#Write a program to remove the duplicate elements from the list 

L = [11,23,4,65,11,15,4]
new = []
for i in L :
	if i not in new :
		new.append(i)
	else :
		continue
print("Original List with duplicates: ",L)
print("New List without duplicates: ",new)

