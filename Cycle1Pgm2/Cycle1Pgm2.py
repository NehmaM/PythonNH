#python program to convert temperature from Celsius to Fahrenheit.

def fahren(cel):
    result=(cel*9/5)+32
    print(f"The {cel} degree Celsius is equal to: {result}-degree Fahrenheit")

cel=float(input("Enter a number"))
fahren(cel)
