#prime number
p = int(input("Enter a Number : ")) 
i = 2
primer=False
while(i < p):
	if(p%i==0):
		primer=True
		break
	else:
		i+=1
if(primer == False):
	print(p," is a Prime Number")
else:
	print(p, " is not a Prime Number")