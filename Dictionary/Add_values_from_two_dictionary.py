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
result = my_dict1.copy()
for key, value in my_dict2.items():
    # If the key already exists in result, add the value from my_dict2 to the existing value in result
    if key in result:
        result[key] += value 
    else:
        result[key] = value

print(result)

# -----------Output section-----------------------
'''
Tescase 1:
-----------
Enter the total number of key-value pairs for first dictionary:4
Enter the key:rahim
Enter the value:12
Enter the key:karim
Enter the value:23
Enter the key:ram
Enter the value:4
Enter the key:sam
Enter the value:5
Enter the total number of key-value pairs for first dictionary:3
Enter the key:karim
Enter the value:15
Enter the key:ram
Enter the value:9
Enter the key:tom
Enter the value:20
{'rahim': 12, 'karim': 23, 'ram': 4, 'sam': 5}
{'karim': 15, 'ram': 9, 'tom': 20}
{'rahim': 12, 'karim': 38, 'ram': 13, 'sam': 5, 'tom': 20}
------------------------------------------------------------------
'''
