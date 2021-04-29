a,b,c = map(int,input('enter three numbers').split())
if a>b and a>c:
    print('a is greatest')
elif b>a and b>c:
    print('b is greatest')
elif c>b and c>a:
    print('c is greatest')
else:
    print('numbers are equal')


#doesnt work when two numbers are equal