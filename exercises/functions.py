# Write your solution for 1.4 here!

def is_prime(x):
	for i in range(x-1,2,-1):
		if(x%1==0):
	print("The number", x, "is a prime number!")
			return False
	return True

a=3	
checking=is_prime(a)
if not checking:
	print("The number", a, "is not prime" )