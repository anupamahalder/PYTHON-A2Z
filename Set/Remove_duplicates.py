# Create an empty list
list1 = []

# Take input for the number of elements in the list
n = int(input("Enter the number of elements for the list: "))

# Input the elements for the list
print("Enter the elements for the list:")
for i in range(n):
    num = int(input())
    list1.append(num)

# Print the list
print("List:", list1)

# put into a set
list1 = set(list1)
# again make it list
list1 = list(list1)

# print the resultant list
print("The output: ", list1)

# --------Output section---------
"""
Enter the number of elements for the list: 7
Enter the elements for the list:
1              
2
3
1
2
3
5
List: [1, 2, 3, 1, 2, 3, 5]
The output:  [1, 2, 3, 5]
"""
