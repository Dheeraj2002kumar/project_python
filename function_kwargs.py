# Function **kwargs

# def thing(name, age=31, *args, **kwargs):
# 	pass



# def person(**kwargs):
# 	print(kwargs)
# 	print(type(kwargs))

# 	if 'age' in kwargs:
# 		print("You are", kwargs.get("name"))
	
# person(name = "Dheeraj", age = 21, brain = "Huge")




# def person(**kwargs):
# 	print(kwargs)
# 	print(type(kwargs))

# 	if 'age' in kwargs:
# 		print("You are", kwargs.get("age"))
	
# person(name = "Dheeraj", age = 21, brain = "Huge")



def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 18.09
    
    for key, value in toppings.items():
        price = price + 2.00
        
    print(f"The total price is ${price}")
    return price

total_price = order_pizza("Saurabh","Canada", jalapenos=True, extra_chees=True, ham=True)
