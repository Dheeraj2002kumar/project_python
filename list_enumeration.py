# List Enumeration & Comprehension

# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

# for animal in animals:
#     print(animal)



# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

# for animal in enumerate(animals):
#     print(animal)




# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

# for index,animal in enumerate(animals):
#     print(index,animal)




# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

# for index,animal in enumerate(animals):
#     if index % 2 == 0:
#         continue
#     print(index,animal)



animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

for index,animal in enumerate(animals):
    # if index % 2 == 0:
    #     continue
    # print(index,animal)
    print(f"{index+1}.\t{animal}")
