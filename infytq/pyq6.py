s = input('enter : ')
lst1 = list(s)
lst2 = ['0','1','2','3','4','5','6','7','8','9']
lst3 = []
for i in lst1 :
    if i in lst2:
        lst3.append(i)
lst3.sort(reverse=True)
length = len(lst3)
flag = 0
if int(lst3[(length-1)]) % 2 != 0 :
    for j in range(length-1,0,-1):
        if int(lst3[j])%2==0:
            flag = 1
            lst3[j] , lst3[(length-1)] = lst3[(length-1)] , lst3[j]
if flag == 0:
    print('-1')
else :
    x = int(''.join(lst3))
    print(x)