def fact(x):
    i=1
    fact = 1 
    while i<=x:
        fact = fact*i
        i=i+1
    return fact

n = int(input('enter a number'))
N = n
temp = 0
n1 = 0
while n>0 :
    temp = int(n%10)
    n1 = n1 + fact(temp)
    n = int(n/10)
print(n1)
if n1==N:
    print('yes it is strong no')
else:
    print('not strong')