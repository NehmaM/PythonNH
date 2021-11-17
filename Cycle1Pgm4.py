list = []

size = int(input("Enter total number of elements"))
for i in range(1,size+1):
    print('Enter {}th element'.format(i))
    n = int(input())
    list.append(n)
print(list)

for i in range(1,len(list)):
    if(list[i]>100):
        list[i] = 'OVER'

print(list)

