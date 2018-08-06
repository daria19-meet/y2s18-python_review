# Part 2 of the Python Review lab.
def is_prime(x):
	for i in range(x-1,2,-1):
		if(x%i==0):
			return False
	return True

def encode(y, x):
	if(y<1 or y>250 or x>1000 or x<500):
		print("Invalid input: Outside range.")
		return None
	checkx=is_prime(x)
	while checkx==False:
		x=x+1
		if(x==1000):
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


def decode(a):
	for y in range(2,250):
		if(is_prime(y)):
			for x in range(500,1000):
				if(is_prime(x)):
					if(y*x==a):
						print("The coded numbers are",x, "and", y )

decode(encode(2,501))