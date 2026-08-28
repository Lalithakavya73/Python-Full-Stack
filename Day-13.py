'''
Range programs
Example:

limit_= 10
for i in range(1, limit_+1):
        for j in range(1, i+1):
            print(j)


limit_= 10
for i in range(2, limit_+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')


limit_= int(input("Enter a number:"))
for i in range(2, limit_+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')

Star programs
Example:
star_= 5
for i in range(1, star_+1):
    for j in range(1, i+1):
        print('*', end=" ")
    print()


star_= int(input("Enter a number: "))
for i in range(1, star_+1):
    for j in range(1, i+1):
        print('*', end=" ")
    print()

star_= int(input("Enter a number: "))
for i in range(1, star_+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Don't repeated values in count outside:

star_= int(input("Enter a number: "))
count=0
for i in range(1, star_+1):
    for j in range(1, i+1):
        count += 1
        print('*', end=" ")
    print()

star_= int(input("Enter a number: "))
count=0
for i in range(1, star_+1):
    for j in range(1, i+1):
        count += 1
        print(j, end=" ")
    print()































