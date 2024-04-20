# Create two empty dictionaries 
my_dict1 = {}
my_dict2 = {}

# Get the number of key-value pairs to add to the dictionary
num_pairs1 = int(input("Enter the total number of key-value pairs for first dictionary:"))

# get the kay-value pair from the user
for i in range(num_pairs1):
    key = input("Enter the key:")
    value = int(input("Enter the value:"))

    # add the key value pair to the dictionary
    my_dict1[key] = value

# Get the number of key-value pairs to add to the dictionary
num_pairs2 = int(input("Enter the total number of key-value pairs for first dictionary:"))

# get the kay-value pair from the user
for i in range(num_pairs2):
    key = input("Enter the key:")
    value = int(input("Enter the value:"))

    # add the key value pair to the dictionary
    my_dict2[key] = value

# print the dictionary 
print(my_dict1)
print(my_dict2)

# make a new dictionary to add values of same key from two dictionaries 
result = my_dict1
for key, value in my_dict2.items():
    # get the value of key from second dictionary if not present 
    # then put a default value as 0 to handle error 
    result[key] = result.get(key, 0) + value

print(result)
