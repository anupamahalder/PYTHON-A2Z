# Problem Statement: Return a list with indices where the value of that index is greater than a target value 

# declare the empty list
list1 = []

n = int(input("Enter the total number of list elements:"))
for i in range(n):
    num = int(input())
    list1.append(num)

target = int(input("Enter the target value:"))

new_lst = [index for index, val in enumerate(list1) if val > target]

print(new_lst)



# ----------Output section-------------
'''
Testcase 1:
-----------
Enter the total number of list elements:6
1
2
3
4
6
5
Enter the target value:3
[3, 4, 5]
'''
