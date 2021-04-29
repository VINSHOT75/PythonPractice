str = input()
lst1 = list(str)
speind = []
spe = []

for i in lst1:
    if i == '@' or i == '#':
        spe.append(i)
        x = lst1.index(i)
        speind.append(x)
lst1 = lst1[::-1]
for i in lst1:
    if i == '@' or i == '#':
        lst1.remove(i)
#print(lst1)
k=0
while k<len(speind):
    lst1.insert(speind[k],spe[k])
    k+=1
str = ''.join(lst1)
print(str)