n = int(input('No of People = '))
r = 2

def fact(x):
    f = 1
    i=1
    while i<=x:
        f = f * i
        i = i + 1
    return f

p = fact(n)//(fact(n-r)*fact(r))
print('factorial : ', p)