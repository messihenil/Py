m,p,c = [int(x) for x in input("Enter the marks for Maths, Physics & Chemistry Sequentially : ").split(" ")]
if m < 35 or p < 35 or c < 35:
	print("You failed in a subject or more!")
else:
	avg = float((m+p+c)/3)
	if avg <= 59:
		print("You got C grade!")
	elif avg <=69 and avg > 59:
		print("You got B grade!")
	elif avg > 69:
		print("Congrats! You got A grade!")