#python program to find the factorial of a number using functions.

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
number = int(input("Enter number to find factorial"))
result = factorial(number)
print("The factorial of %d=%d"%(number,result))
