n=int(input("enter a number:"));
for i in range(2,n):
	if(n%i==0):
		print("it is not a prime number")
		break
if(i==n-1):
	print("it is prime number")
