n = int(input('No of students = '))
r = int(input('No of seats = '))

def fact(x):
    f = 1
    i=1
    while i<=x:
        f = f * i
        i = i + 1
    return f

p = fact(n)//fact(n-r)
print('factorial : ', p)