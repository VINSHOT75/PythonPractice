a = int(input('enter a number'))
x=1
re=0
while a>0 :
    x=a%10
    if x==0:
        x=1
    elif x==1:
        x=0
    re = re*10 + x
    a =a//10
rev = 0
while re>0 :
    rev = int(re%10)
    print(rev , end='')
    re= re//10
