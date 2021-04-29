str = input('enter : ')
values = list(str)
print(values)
lst = []
length = len(values)
for i in range(0,(length-1)):
    lst.append(values[i])
    for j in range(1,(length-1)):
        if values[i] == values[j]:
            #print(lst)
            break
        else:
            lst.append(values[j])
        
    break
x= ''.join(lst)
print(x)

