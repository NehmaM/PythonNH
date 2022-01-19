#python program to generate all factors of a number.

def factor(x):
    print("The factors of",x,"are:")
    for i in range(1,x+1):
        if x % i == 0:
            print(i)


num = int(input("Enter a number to generate all factors of the number"))
factor(num)
