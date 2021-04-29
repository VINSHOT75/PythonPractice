stack = []
count = 0
str = input()
for i in str :
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
        count = count+1
    elif i == ')' or i == '}' or i == ']':
        if count == 0:
            print('no brackets ')
        elif count>0:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
if not stack:
    print('no problem') 
else:
    print(f"problem is at {count}")
print(str)
print(stack)