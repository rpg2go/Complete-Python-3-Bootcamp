for item in range(2, 10):
    print(item)
else:
    print('end first for loop')

for item in range(2, 10):
    if item % 2 == 0:
        print(item)
    elif item % 3 == 0:
        print(f'A number modulo 3  is {item}')
else:
    print('end second for loop')

mylist = list(range(0, 12, 2))
print(f'My list is : {mylist}')
    





