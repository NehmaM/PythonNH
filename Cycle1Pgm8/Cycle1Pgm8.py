
y={'carl':40 , 'alan':2, 'bob':1,'danny':3}
l=list(y.items())
l.sort()
print('Ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)
dict=dict(l)
print("Dictionary",dict)

'''

dict1 = {'wwww':80,'zzzzzzz':78,'Aaabc':32,'aaaaabc': 1}
print(dict1)
print("\ndict.keys():{}".format(dict1.keys()))
print("\ndict.values():{}".format(dict1.values()))
print("\ndict.items()-sort it by keys and return a list of tuples:{}".format(dict1.items()))


# " No matter what iterable is passed in to the sorted() function, it always returns a list."

kdict = sorted(dict1.keys())
print("\n\nsorted(dict1.keys()) - Dictionary sorted based on keys:{}".format(kdict))


vdict = sorted(dict1.values())
print("\nsorted(dict1.values())- Dictionary returning list of values:{}".format(vdict))

print("\n\nSorted(dictionary name) function")
dictionary= sorted(dict1)
# "if we pass in the entire dictionary as the iterable to the sorted() function, it returns a list that contains only the keys sorted alphabetically.")
print("\nsorted(dict1):{}".format(dictionary))


#items(): to get a sorted copy of the entire dictionary")



'''
