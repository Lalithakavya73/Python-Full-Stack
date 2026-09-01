'''
words = 'madam'
empty_str = ''
for i in words:
    empty_str = i + empty_str
if empty_str == words:
    print(f"{words} is a palindrome ")
else:
    print(f"{words} is not a palindrome ")
    
-->
words = input("Enter a words:")
empty_str = ''
for i in words:
    empty_str = i + empty_str
    print(empty_str)
if empty_str == words:
    print(f"{words} is a palindrome ")
else:
    print(f"{words} is not a palindrome ")

Amstrong Number
---------------
153 --> 1 + 5 + 3
1634 --> 1 + 6 + 3 + 4
num = int(input("Enter a number:"))
length_ = len(str(num))
amstrong_ = 0
for i in str(num):
    amstrong_ = amstrong_ + int(i)**length_
    print(amstrong_)
if amstrong_ == num:
    print(f'{num} is Amstrong Number')
else:
    print(f'{num} is Not Amstrong Number')
 
Perfect Number
--------------
1 + 2 + 3 = 6
1 + 2 + 4 + 7 + 14 =28
Example:
num = int(input("Enter a number:"))
any_ = 0
for i in range(1,num):
    if num % i == 0:
        any_ += i
if any_ == num:
    print(f'{num} is Perfect Number')
else:
    print(f'{num} is Not Perfect Number')
    
-->
num = 28
for i in range(1,num):
    print(i)
    
-->
num = 28
sum_ = 0
for i in range(1,num):
    if num % i == 0:
        sum_ += i
if sum_ == num:
    print(f'{num} is Perfect Number')
else:
    print(f'{num} is Not Perfect Number')

Fibanocci Series
----------------
Exanple:
num = 0
num_2 = 1
print(num,num_2)
for i in range(1,10):
    pass
    
-->
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3, end=' ')
    























