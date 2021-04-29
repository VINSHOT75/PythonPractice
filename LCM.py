a,b = map(int, input('enter two numbers : ').split())
i=1
x=a
y=b
lis1 = []
lis2 = []
while i< 10:
    x = a*i
    lis1.append(x)
    #print('x  ',x)
    y = b*i
    lis2.append(y)

    #print('y  ',y)

    i=i+1
print(lis1)
print(lis2)
i=0
j=0
#print(len(lis1))
#print(len(lis2))
while i<len(lis1):
    while j<len(lis2):
        if lis1[i]==lis2[j]:
            print(lis1[i])
            break
       # print(j)
        j=j+1
    #print(i)    
    i=i+1






#num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))


#def lcmFinder(num1, num2):
   # if num1 > num2:
   #     larger = num1
   # else:
   #     larger = num2
   # while True:
   #    if (larger % num1 == 0) and (larger % num2 == 0):
   #         lcm = larger
#          break
#       larger = larger + 1
#    print("LCM of two given number:{}".format(lcm))


#lcmFinder(num1, num2)
