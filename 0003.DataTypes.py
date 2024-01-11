# -----------------string type data----------------------
book = "Hello World"
print(type(book))

# -----------------number type data----------------------
num1 = 45
print(type(num1))

# -----------------floating type-------------------------
num2 = 34.9
print(type(num2))

# ----------------complex datatype----------------------- 
num = 42j
print(num)
print(type(num))

# ----------------boolean datatype-----------------------
Bool = True
print(Bool)
print(type(Bool))
print(7==9) #False

# ---------------Binary types----------------------------
#-----------bytes()--------------
myList = [1,4,5,34,55,122]
b = bytes(myList)
print(type(b)) #<class 'bytes'>
# we cannot modify the bytes object 
# b[0] = 9 # X
# ----------bytearray()----------
# binary type data
yourList = [14,76,5,34,55,122]
b1 = bytearray(yourList)
print(type(b1)) #<class 'bytearray'>
# we can modify the bytearray 
b1[0] = 9 # X

# ---------------None type-------------------------------
x = None
print(x) #None
print(type(x)) #<class 'NoneType'>

# ---------------Sequence type----------------------
# --------list type data----------
li = ["Tom","Ram","Piya","Uma"]
print(li) #['Tom', 'Ram', 'Piya', 'Uma']
print(type(li)) #<class 'list'>
# list data can be modifiable
li[1] = "Rom"
print(li) #['Tom', 'Rom', 'Piya', 'Uma']

# --------tuple type data-----------
tup = (4, 5, 6, 3)
print(tup) #(4, 5, 6, 3)
print(type(tup)) #<class 'tuple'>
# tuple data cannot be changed 
# tup[1] = 100 # X

# ----------Range type data---------
ran = range(6)
print(ran) #range(0, 6)
print(type(ran)) #<class 'range'>
for i in ran:
    print(i) # 0 1 2 3 4 5 



'''
  ========================OUTPUT SECTION==========================
  <class 'str'>
  <class 'int'>
  <class 'float'>
  <class 'complex'>
  <class 'bool'>
'''
