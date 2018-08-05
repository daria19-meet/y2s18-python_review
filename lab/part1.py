# Part 1 of the Python Review lab.

def hello_world():
	print("Hello World!")

hello_world()

def greet_by_name(name):
	print("Hello",name)

greet_by_name("Daria")

def encode(x):
	return x*3953531



def decode(coded_message):
	print(coded_message/3953531)

decode(encode(2))