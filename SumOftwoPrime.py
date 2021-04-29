a = int(input('enter number : '))
li = []
def pri(x):
    i = 2
    if x==0 or x==1 :
            print('neither prime nor composite')
    else :
        while i<=x :
            if x % i == 0 :
                if x==i :
                    #print('prime')
                    return True
                else :
                    return False
                    #print('not prime')  
            i = i+1 
#xyz = pri(2)
#print(xyz)
i=2
#print('a = ',a)
while i<a:
    #if a%i==0:
    check = pri(i)
    #print(check)
    if check==True:
        li.append(i)
    i=i+1 
print(li)

i=0

while i<len(li):
    j=0
    while j<len(li):
        #print('i = ',i)
        #print('j = ',j)
        if li[i]+li[j]==a :
            print(li[i],'-',li[j])

        j=j+1
    i=i+1
  