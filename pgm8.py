n=int(input('enter a number:'))
m=n
rev = 0
while(n>0):
    rem=n%10;
    n=int(n/10);
    rev=rev*10+rem

print(m)
print(rev)
if(m==rev):
    print('palindrom')
else:
    print('Not a palindrome')
