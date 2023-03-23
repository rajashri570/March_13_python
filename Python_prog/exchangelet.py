#write A program to exchange the first and Last letter of string 

s1 = "Shrikant"
print(" String before exchange of letters : " , s1)

l = list(s1)
print(l)

ln = len(l)

l[0] , l[ln-1] = l[ln-1] , l[0]

s2 = ''.join(l)

print(" After exchange letters: ",s2) 



