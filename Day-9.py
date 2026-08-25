'''
set
---
--> Set is unordered collection of elements
--> No duplicate allowed in the set
--> Set is represented by {}
example:
nums = {1,2,3,2}
print(nums)

Operations
----------
--> The union() will combine two set into a single set
Syntax --> Set_1.union(set_2) or set_1 | set_2 
Example:
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.union(nums))
print(data_ | nums)

Intersection
------------
--> This will gives us the common elements from both sets
Syntax --> Set_1.inersection(set_2) or set_1 & set_2
Example:
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.intersection(nums))
print(data_ & nums)

Difference:
-----------
--> IT will display the different elements from set_1, but not the set_2 elements
Syntax --> Set_1.difference(set_2) or set_1 - set_2
Example:
data_ = {1,2,3,4}
nums = {4,5,6}
print(nums - data_)
print(nums.difference(data_))

Symmetric_difference()
----------------------
--> Different elements from the both
Syntax --> Set_1.Symmetric_difference(set_2) or set_1 set_2
Example:
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.symmetric_difference(nums))

Methods
-------
1.add()
-------
--> add() method will be add only one element at a time
Syntax --> set.add(element)
Example:
data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)

Update()
--------
--> We can add more one elements by using update method
Syntax --> Set.update([elements]) or set_1.update(set_2)
Example:
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)

Remove()
--------
--> Remove method will delete the given element from the set
--> If the element is not present in the set
--> it will raise error
Syntax --> Set.remove(element)
Example:
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)

Discard()
---------
--> The method is used to delete the elements from the set, but never raise any error even the element not inside set
Syntax --. set.dicard(element)
example:
data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)

Clear()
--------
--> The methods is used to delete all elements from the set and it will written empty set
Syntax --> set.clear()
Example:
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)









