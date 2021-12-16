name = raw_input("Enter a string")
name.split()
vow=['a','e','i','o','u']

listComp=[char for char in name if char in vow]
print("List of vowels in {} is {}".format(name,listComp))





'''
name = "hello"
name.split()
mylist=[]
vow=['a','e','i','o','u']

for char in name:
        if char in vow:
                mylist.append(char)
	

print("Original list",name)
print(mylist)

'''


#words_starting_with_vowel = [word for word in words if word[0] in 'aeiou']
