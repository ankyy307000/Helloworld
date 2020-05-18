
def convert(num): 

	 
	if num == 0: 
		return 0

	 
	digit = num % 10

	if digit == 0: 
		digit = 5

	
	return convert(num // 10) * 10 + digit 

def change(num): 
	if num == 0: 
		return 5
	else: 
		return convert(num) 


num = int(input("Enter a number :"))
print (change(num)) 

