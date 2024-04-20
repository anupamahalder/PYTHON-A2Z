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

# Sort the list
list1.sort()

# Print the second highest number from the list
if len(list1) >= 2:
    print("Second highest:", list1[-2])
else:
    print("There are fewer than two elements in the list.")




# -------Output section-------
''' 
Testcase 1: 
------------
Enter the number of elements for the list: 5
Enter the elements for the list:
23 
34 
6
7
4
List: [23, 34, 6, 7, 4]
Second highest: 23

------------------------------------------
Testcase 2:
-------------
Enter the number of elements for the list: 1
Enter the elements for the list:
23
List: [23]
There are fewer than two elements in the list.
'''
