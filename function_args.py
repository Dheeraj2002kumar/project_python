# Function *ARGS

def add_numbers(*args):
	total = 0
	for num in args:
		total += num
	return total

total = add_numbers(1,2,3,4,5)
print(total)