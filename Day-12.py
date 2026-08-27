'''
Loops
-----
For loop --> For loop is used to iterate over a sequence on iterable datatypes
Example:
nums = [12,3,5,78]
for num in nums: # num is define this variable at run to start values from iterable datatype
    print(num)

else in for
-----------
If-Else --> Unlike if-else, else block in for statement is excuted after completed of all iterations
Example:
nums = 'Python'
for num in nums:
    print(num)
else:
    print('For ended')

Control Statments
Break
-----
--> The break used to stop iteration based on the condition given
Example:
nums = [1,2,3,4,5,8,9]
for num in nums: 
    print(num)
    if num == 3: 
       break

val_ = [1,2,3,4,5,8,9]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is Even')
    else:
        print(f'{j} is Odd')

Continue
--------
--> The continue is keyword used to skip the current iteration based on the condition
Example:
nums = [1,2,3,4,5,8,9]
for num in nums: 
    if num == 5: 
       continue
    print(num)
    
Pass
----
--> A pass is called as space-holder, that is used after statements like (if, for, else) not to raise any error 
Example:
for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass

Assertion
---------
--> Assertion is a keyword used to check the condition, incase the condition is false, it will raise the error(AssertionError)
Example:
age = 15
assert age>= 18, 'Not eligible to vote'
print('Your eligible to vote')
   and
age = 19
assert age>= 18, 'Not eligible to vote'
print('Your eligible to vote')
   
While loop
Example:
num = 1
while num < 5: # 1<5
    print(num)
    num += 1


num = int(int("Enter "))
count = 0
for j in range(1, num+1):
    if num % j == 0:
        count += 1
        print(count)
        

























