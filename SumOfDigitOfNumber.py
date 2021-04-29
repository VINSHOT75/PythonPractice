a = int(input('enter a number'))
s= 0
i=0
while i<3 :
    s = s + a%10
    a= a/10
    i=i+1
print(s) 

#don