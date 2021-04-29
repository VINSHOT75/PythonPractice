x = int(input('enter a number : '))
y=x
i=0
a=0
while x>0 :
    a = a + int(x%10)
    x = int(x/10)
if y%a == 0:
    print('harshad')
else : 
    print('not harshad')