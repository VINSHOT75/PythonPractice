# armstrong number
num = int(input('enter the number'))
x= num
y=0
z=0
while  x>0 :
    y =int( x%10)
    z = z+(y*y*y)
    x =int(x/10) 
print(z)
if z == num :
    print('armstrong')
else:
    print('not armstrong')