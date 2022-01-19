# python program to check whether a given string is palindrome or not

def Palindrome(st):
    return st == st[::-1]

stg=input("Enter string:")
palin = Palindrome(stg)
    
if palin:
    print("Yes")
else:
    print("No")
