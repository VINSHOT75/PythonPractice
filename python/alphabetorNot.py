n=input() 
#ASCII value of the input 
x=ord(n)
if(65<=x<=90 or 97<=x<=122):
    print('is an Alphabet')
else:
    print('is not an Alphabet')