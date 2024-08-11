
n=int(input('enter a number:'))
def fact(n):
    print("calling fact for %s"%n)
    
   # if(n==1):
    #    return 1;
    return n*fact(n-1)
print(fact(n))









    

