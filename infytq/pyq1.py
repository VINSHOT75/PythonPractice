inp = input()
print(inp)
lst = inp.split(',')
lst2 = []

print(lst)

for x in lst :
    a = x.split(':')
    #print(a)
    lst2.append(a)
print(lst2)
for i in lst2:
    lst3 = []
    for j in i[1]:
        #print(f"value{j}")
        
        if len(i[0])>=int(j):
            lst3.append(j)
            x = int(max(lst3))
    print(lst3)
    try:
        for k in i[0]:
            op = k[x]
    except:
        print('ex')
        op = 'X' 
    #print('')
    print(op,end='')

