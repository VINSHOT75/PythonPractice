a = int(input('enter a binary number : '))
i=0
s=0
while a>0:
    r =  a % 10
    s = s+ r*pow(2,i)
    a=a//10
    i=i+1
print(s) 