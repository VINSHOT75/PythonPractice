x = int(input('enter a number'))
a= 0
b=1
if x>0:
    print('0 ,',end='')
if x>1:
    print('1 ',end='')

i=0
while i<x :
    c=a+b
    print(',',c,end='')
    a=b
    b=c
    i=i+1
