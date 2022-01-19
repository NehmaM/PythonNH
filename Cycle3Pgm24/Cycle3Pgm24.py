# python program to accept a list of words and return the length of the longest
#word.

def Llength(alist):
    maxLength = len(a[0])
    temp = a[0]

    for i in alist:
        if(len(i) > maxLength):
            maxLength = len(i)
            temp = i
            
    print(f"The word {temp} have the longest length {maxLength}")

a=["animate","development","self"]
print("List : {}".format(a))
Llength(a)
