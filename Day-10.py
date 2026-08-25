'''
Dictionary
----------
--> Dictionary is a collection of key: Value pair
--> Key most be unique and it should be immutable datatype(int, string, tuple)
Example:
details = {1:2,
           'name': 'Kavya',
           (1,2): [1,2]}

Accessing
---------
--> Dictionary can access by calling key, we will get value from that key
Syntax --> Dictionary['key']
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y'}
print(data_['Aadr'])

get()
----
--> get() method is also used to get the value from the key
Syntax --> dict.get(key)
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         2:[3,4]}
print(data_['Aadr'])
print(data_.get(2))

Update()
--------
--> Method is used update a key, incase if the key is not present inside dict then it add that key: value
Syntax--> dict.update({'key':value})
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         2:[3,4]}
print(data_)         
data_['name'] = 'Chakri'
print(data_)

--> There is another way to update a key
Syntax --> dict[key] = value
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         2:[3,4]}
print(data_)         
data_['AC'] = 2003274526
data_.update({'name':'chakri'})
print(data_)


Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y'}
print(data_)         
data_['AC'] = 2003274526
data_.update({'name':'chakri'})
data-.update({'ATMPIN':2703})
print(data_)

Values()
--------
--> Values() method is used get all the value from the dictionary
Syntax --> dict.values()
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         }
print(data_.values())  

Keys()
------
--> keys() method is used get all the key from the dictionary
Syntax --> dict.keys()
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         }
print(data_.keys())  

items()
-------
--> The method will get the kay:value separated from the dictionary
Syntax --> dict.items()
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         }
print(data_.items())  

Clear()
-------
--> clear() method is used to delete all data from dictionary
Syntax --> dict.clear()
Example:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         }
print(data_)
data_.clear()
print(data_)

Delete()
--------
--> 
Syntax --> dict.delete()
Exampple:
data_ = {'name':'Kavya',
         'balance':7000,
         'Aadr':123345678945,
         'PANC':'GPXBP2890Y',
         }
print(data_)
del data_['Aadr']
print(data_)
data_.clear()
print(data_)

Statements:
If statement
------------
--> If condition become  true, then it will excute inside block of code
--> Incase it becomes false, then it will never entry inside block
Example:
age = 15
if age>=18:
   print('Eligible to vote')
print(age)

age = 19
if age>=18:
   print('eligible to vote')
   print(age)

a = 90
b = 78
if a>b:
   print(a)

If-Else
-------
--> Else for if statement is a fall-block statement, incase if condition is false then else block will excuted
Example:
age = 15
if age>=18:
   print(f'your {age} Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')

a = 90
b = 780
if a>b:
   print(a)
else:
    print(b)





















