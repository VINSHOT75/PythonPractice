a,b = map(int, input('enter first fraction').split('/'))
c,d = map(int, input('enter second fraction').split('/'))

if b==d :
    sum = a+c
    print('sum = ',sum, '/' ,d)


elif b!=d :    
    sum = ((a*d)+(b*c))
    den = (b*d)
    print('sum = ',sum, '/' ,den)
    