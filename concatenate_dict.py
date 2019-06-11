#Learning dictionary basics. Also find a solution to concatenate two dictionaries!!!i
#Dictionaries in python are data structures which contains data as key value pairs and are seperated by commas
#All keys in a dictionary should be unique

dict1={"name":"Arnab","age":30,'a':255,'x':128}
dict2={"name":"Deepak","age":25,'b':155}

#concatenate two dictionaries
'''
>>> dict1+dict2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
'''
#correct way to concatenate two dictionaries
#Updates the value of same key(name and age) to the value of dict2. 
dict1.update(dict2)

#To find length of a dictionary
l1 = len(dict1)
l2 = len(dict2)
print("Length of dict1: ",l1,"Length of dict2: ",l2)

#Print Dictionies
print("dict1= ",dict1,"dict2= ",dict2)

print("Concatenated List!!!")
print(dict1)

#How to itterate through key values in a dictionary
print("Keys of dict1:-")
for i in dict1:
    print(i,end ="\t")
print()

#how to itterate through values in a dictionary
print("Values of dict1:-")
for i in dict1.values():
    print(i,end ="\t")
print()
