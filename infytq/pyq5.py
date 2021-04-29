s = input('str = ')

lst1 = list(s)
x = len(s)
count = 0
lst2 = []
lst3 = []
print(lst1)
for i in range(x//2,0,-1):
    lst2.append(lst1[i-1])
    #print(f"i = {i}")
for j in range(x,x//2,-1):
    lst3.append(lst1[j-1])
    #print(f"j = {j}")
print(lst2)
print(lst3)

#for i in lst2 :
    

print(count)