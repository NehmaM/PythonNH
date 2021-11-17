list1 = []
oddlist= []

size = int(input("Enter total number of elements of initial list"))
for i in range(1,size+1):
    ele = int(input("Enter {}th element".format(i)))
    list1.append(ele)
print("initial list: {}".format(list1))

for n in list1:
    if(n%2!=0):
        oddlist.append(n)
            
print(" odd list: {}".format(oddlist))

