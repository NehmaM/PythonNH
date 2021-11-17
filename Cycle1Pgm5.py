list1 = []
list2 = []
sum1 = 0
sum2 = 0

#prompting user to enter 2 list of integers
print("prompting user to enter 2 list of integers")

size1 = int(input("Enter total number of elements in list1"))
for i in range(0,size1):
    ele1 = int(input("Enter {}th elements of list 1".format(i)))
    list1.append(ele1)

size2 = int(input("Enter total number of elements in list2"))

for i in range(0,size2):
    ele1 = int(input("Enter {}th elements of list 2".format(i)))
    list2.append(ele1)

print("List1: {}".format(list1))
print("List2: {}".format(list2))

#Checking whether lists sum to same value
print("---------------------------------------------------------------")
print("Checking whether lists sum to same value")
for i in list1:
    sum1 = sum1+ i
    
for i in list2:
    sum2 = sum2+ i

print("sum of list 1:{}".format(sum1))   
print("sum of list 2:{}".format(sum2))

if(sum1==sum2):
    print("List1 and List2 are of same length")
else:
    print("List1 and List2 are of different length")

#Checking sum of list using inbuilt sum()
print("---------------------------------------------------------------")
print("Checking sum of list using inbuilt sum()")
print(sum(list1))
print(sum(list2))

#checking whether lists are of same length using len()
print("---------------------------------------------------------------")
print("checking whether lists are of same length using len()")
print("Length of list1: {}".format(len(list1)))
print("Length of list2: {}".format(len(list2)))

#Checking whether any common value occurs in both list
print("---------------------------------------------------------------")
print("Checking whether any common value occurs in both list")
list1_set = set(list1)
list2_set = set(list2)

if(list1_set & list2_set):
    print("common elements found:{}".format(list1_set & list2_set))
else:
    print("No common elements")

