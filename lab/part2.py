# Part 2 of the Python Review lab.

def encode(x, y):
	if(y<1 or y>250 or x>1000 or x<500):
		print("Invalid input: Outside range.")
		return None
	checkx=is_prime(x)
	while checkx==False:
		x=x+1
		if(x=1000):
			print("Invalid input: Outside range.")
			return None	
		checkx=is_prime(x)

	checky=is_prime(y)
	while checky==False:
		y=y+1
		if (y==250):
			print("Invalid input: Outside range.")
			return None
		checky=is_prime(y)
	return x*y

def is_prime(x):
	for i in range(x-1,2,-1):
		if(x%i==0):
			return False
	return True

def decode(coded_message):
	pass