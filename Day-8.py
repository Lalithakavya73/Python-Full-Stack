'''
Tuple
-----
--> Tuple is collection of different datatypes that separated bu, and repersented bu()
--> It is immutable
--> We can pass a tuple values and that can be asign to the variables, but should match same number variables and values inside the tuple
Example:
t = (1, 'Python', [3,4], (7,9))
print(t[2][1])

Indexing
--------
--> If the item is not present int tuple, it will raise valueError
Example:
t = (1, 'Python', [3,4], (7,9))
print(t.index('Python'))

length
------
--> 
Example:
t = (1, 'Python', [3,4], (7,9))
print(len(t))

Accessing through Tuple
name, age, batch, dept = ('Kavya', 23, 5, 'Python')
print(name)
print(age)
print(batch)
print(dept)

Max()
-----
--> Used to fond out the max value from the tuple
Example:
so = (67,5,89,45)
print(max(so))

Min()
-----
--> Used to find out the least value from the tuple
Example:
so = (67,5,89,45)
print(min(so))

Count()
-------
--> Used to count an item present in the tuple
Example:
so = (67,5,89,45,5)
print(so.count(5))

Do
so = (67,5,89,45)
do = (45,89)
print(so+do)
