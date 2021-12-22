#single string seperated with space from two strings by swapping the character at position 1.

str1 = raw_input("Please Enter First String : ")
str2 =raw_input("Please Enter Second String : ")
 
#swap first two characters of given string
x = str2[:1] + str1[1:]
y = str1[:1] + str2[1:]
 
#print result
print("Your first has become :- ",x)
print("Your second has become :- ",y)









'''

str1 = raw_input("Please Enter First String : ")
str2 =raw_input("Please Enter Second String : ")
 
x=str1[0:1]
 
str1=str1.replace(str1[0:1],str2[0:1])
 
str2=str2.replace(str2[0:1],x)
 
print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)

o/p err
'''
