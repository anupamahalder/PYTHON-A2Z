# List 
li = ['a', 'b', 'c', 1, 3, "hello", "world"]

# find type of li 
print(type(li)) #<class 'list'>

#print the entire list 
print(li) #['a', 'b', 'c']

# print only one item from the list by index of list
print(li[3]) #1
print(li[2]) #c

# Using index of list we can add/remove/update our list items

# change/modify the value of index 2 
li[2] = 'cat'
print(li) #['a', 'b', 'cat', 1, 3, 'hello', 'world']

#--------------List of string ----------------------
newList = ["anu","pama","rup","halder"]
print(newList) #["anu","pama","rup","halder"]

#-------------List of boolean-----------------------
myList = [True, False, True, True]
print(myList) #[True, False, True, True]

# ============Access list items=================== 
myName = newList[0]
print(myName) #anu

mySurname = newList[3]
print(mySurname) #halder

# =============Change list items===================
newList[0] = "anupama"
print(newList) #['anupama', 'pama', 'rup', 'halder']

# ================Add list items================== 
# Add list items with append()
newList.append("Priya")
print(newList) #['anupama', 'pama', 'rup', 'halder', 'Priya']

# Add list items with insert()
newList.insert(1,"Google")
print(newList) #['anupama', 'Google', 'pama', 'rup', 'halder', 'Priya']

# ================Remove list items================
list1 = ["a", "b","c", "d"]

# remove with remove() method 
list1.remove("b")
print(list1) #['a', 'c', 'd']

li.remove(3)
print(li) #['a', 'b', 'cat', 1, 'hello', 'world']

# remove with pop() method
list1.pop(2)
print(list1) #['a', 'c']

list1.pop()
print(list1) #['a']

# delete item with del keyword by providing index
del li[3]
print(li) #['a', 'b', 'cat', 'hello', 'world']

# Clear() method
list1.clear()
print(list1) #[]



