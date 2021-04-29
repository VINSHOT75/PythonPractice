x = int(input('enter a number'))
rev = 0
while x>0 :
    rev = int(x%10)
    print(rev , end='')
    x= int(x/10)

