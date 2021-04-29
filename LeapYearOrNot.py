a = int(input("enter year"))
if a%4==0 :
    if a%400 == 0 :
        print("leap year")
    elif a%100 == 0 :
        print('not leap year')
    else:
        print('leap')    
else :
    print('not leap')            
