''''
a=set([10,20,30,40,50])
print(a)
a.add(78)
a.add(50)
print(a)
a.remove(20)
print(a)
a.discard(30)
print(a)
b = set([40,50,60,70,80])
print(b)    
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
'''
'''
# Accesing of tuple:
t =(1,2,3,4,5)
print(t[0])  #Error

#4) Concatenation of tuple:
t =(1,2,3,45,50)
t2 =(2,3,547,8)
print(t+t2)

#5) Repetition of tuple:
t =(1,2,3,45,50)
print(t*3)

#6) Nesting of tuple:
t =(1,2,3,45,50)    #t=(1,2,(3,4,5),8)
t2 =(2,3,547,8)
print(t,t2)

#7) slicing of tuples:
t =(1,2,3,45,50)
print(t[1:])
print(t[0:3])

#8) Deleting of tuple:
t =(1,2,3,45,50)
del t
print(t)

#9) Leetcode problems on tuples(349,657) 
'''

#3) Creation ({},dict())

d = {"name": "Sai",'age':19}
print(d.get("name"))
print(d.keys())
print(d.values())

#4) Adding & Updating dict items

d = {"name": "Sai",'age':19}
d['phn'] = 46432
print(d)
d['age'] = 20
print(d)

#5) Removing dict items(del,pop(),popitem(),clear())

d = {"name": "Sai", 'age': 19}
print(d)
del d['age']
print(d)
d.pop('name')
print(d)
d.popitem()
print(d)
d.clear()
print(d)