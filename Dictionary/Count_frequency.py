# declare the empty list
list1 = []

n = int(input("Enter the total number of list elements:"))
for i in range(n):
    num = int(input())
    list1.append(num)

# make it like a map where key will be the element and the occurances will be the value 
dict1 = { item:list1.count(item) for item in list1}
print(dict1)

# -----------Output section---------------
"""
Testcase 1:
-----------
Enter the total number of list elements:10
1
2
3
1
2
3
1
5
6
1
{1: 4, 2: 2, 3: 2, 5: 1, 6: 1}
"""
