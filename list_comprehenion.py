# List comprehenion

# numbers = []
# for num in [1,2,3,4,5]:
#     numbers.append(num**2)
# print(numbers)

# # this code is list comprehenion-----------------------------
# numbers = [num**2 for num in [1,2,3,4,5]]
# print(numbers)


# Dictionary Comprehension----------------------------------------

names = [("name", "Dheeraj"), ("occupation", "coder")]
d = {}   # d is looking like a dictionary comprehension
for key, value in names:
    d[key] = value
print(d)
print(type(d))


# this code is dictonary comprehension---------------------

d = {key: value for key, value in names}
print(d)



d = dict(names)
print(d)
