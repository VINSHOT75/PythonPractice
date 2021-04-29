x = int(input('enter a number'))
num = x
rev = 0
temp = 0
while x>0 :
    temp = int(x%10)
    rev = (rev*10) + temp
    x= int(x/10)
if rev==num :
    print('palindrome')
else:
    print('no palindrome')
