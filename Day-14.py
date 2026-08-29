'''
In string
---------
Example:
ran_ = int(input("Enter a number:"))
for j in range(1, ran_+1):
    if j % 2 == 0:
       print(f'{j} is even')
    else:
        print(f'{j} is odd')

In list
-------
Example:
nums = [23,78,97,5]
for j in nums:
    if j % 2 == 0:
       print(f'{j} is even')
    else:
        print(f'{j} is odd')

words_ = input("Enter a word: ")
vowels = 'aeiouAEOIU'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)

words_ = input("Enter a word: ")
vowels = 'aeiouAEOIU'
count = 0
for i not in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)

Remove duplicates list
----------------------
Example:
digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)


digits_ = [1,2,3,1,5,3,7,2]
digits_tuple = tuple(set(digits_))
digits_ = list(digits_tuple)
print(digits_)










































