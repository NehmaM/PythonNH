#merging 2 dictionaries

def merge(dict1,dict2):
    z=dict1.copy()
    z.update(dict2)
    return z

if __name__=="__main__":
    dict1={'x':1,'y':2}
    dict2={'a':3,'b':4}
    merged_dict=merge(dict1,dict2)
    print(merged_dict)






























'''
def dictMerge(d1,d2):
    d3={}
    for ad1 in d1:
        if ad1 not in d2:
            d3.append(ad1)
    return d3


d1={1:'aaa' , 2:'bbb' , 3:'ccc'}
d2={4:'ddd' , 5:'eee' , 6:'fff' , 1:'aaa' , 2:'bbb'}

print("\nBefore merging: d1 is",d1)
print("\nBefore merging: d2 is",d2)

dictMerge(d1,d2)

print("\nAfter merging d1 is",d1)
print("\nAfter merging d2 is",d2)

print("\nd3=",d3)




def DictListUpdate( lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

x = [ {"name": "surya", "company":"dell"}, \
       {"name": "jobs", "company":"apple"} ]

y = [ { "name": "surya", "company":"dell"}, \
    { "name": "gates", "company": "microsoft"} ]

print DictListUpdate(x,y)



def dictMerge(d1,d2):
    d3={}
    for ad1 in d1:
        if ad1 not in d2:
            d3.append(ad1)
    return d3


d1=[ {"name": "surya", "company":"dell"}, \
       {"name": "jobs", "company":"apple"} ]

d2=[ { "name": "surya", "company":"dell"}, \
    { "name": "gates", "company": "microsoft"} ]

print("\nBefore merging: d1 is",d1)
print("\nBefore merging: d2 is",d2)

dictMerge(d1,d2)

print("\nAfter merging d1 is",d1)
print("\nAfter merging d2 is",d2)

print("\nd3=",d3)

'''
