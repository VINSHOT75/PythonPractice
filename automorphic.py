num = int(input('enter a number : '))
x = num*num
y = num%10
z = x%10
if y==z:
    print('automorphic')
else:
    print('not automorphic')