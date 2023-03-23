'''#Write a program to reverse the string 
'''

str = input("Enter string: ")
reverse = ''
for i in range(len(str), 0, -1):
      reverse += str[i-1]

if str == reverse :
	print(f"{str} is palindrome string")
else :
	print(f"{str} is not palindrome string")
