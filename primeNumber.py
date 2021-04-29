a = int(input("enter no : "))
i = 2
if a==0 or a==1 :
    print('prime')
else :
    while i<=a :
        if a % i == 0 :
            if a==i :
                print('prime')
            else :
                print('not prime')
                break   
        i = i+1 
