x=int(input('enter  a:'))
i=1
z=0
while i<=x :
    if x%i == 0:
        z=z+i
        print(z)
    i=i+1
print(z)
if z == x :
    print('perfect')
else:
    print('not perfect')