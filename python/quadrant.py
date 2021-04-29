a , b = map(int,input('enter two numbers').split())

if a>0 and b>0 :
    print('First quadrant')
elif a<0 and b>0 :
    print('Second quadrant')
elif a<0 and b<0 :
    print('Third quadrant')
elif a>0 and b<0 :
    print('Fourth quadrant')

else:
    print('orgin')