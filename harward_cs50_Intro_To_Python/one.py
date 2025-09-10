try:
	x = float(input("What's x? "))
	y = float(input("What's y? "))
	z = round(x + y)
	print(f"{z:,}")
except ValueError:
	print("Please enter valid numbers for x and y.")