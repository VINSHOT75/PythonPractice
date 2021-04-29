def factor(x):
    factorials = []
    i=1
    while i<x:
        if x%i==0:
            factorials.append(i)
        i=i+1
    return factorials 

a,b = map(int , input('enter a two numbers - ').split())
lis1 = factor(a)
lis2 = factor(b)
print(lis1)
print(lis2) 
i=0
lis3 = []
while i<len(lis2):
    if lis1[i] == lis2[i]:
        lis3.append(lis1[i])
    i=i+1
print(lis3)

#not correcct