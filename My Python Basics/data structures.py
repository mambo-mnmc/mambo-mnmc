# to use create arrays in python
from array import *
ndila=array('i', [2, 4, 6, 8, 10]) #array has been created

#insert item in array
ndila.insert(3, 12)
ndila.append(60)
#remove item in array
ndila.remove(2)
print (ndila.index(4))
#searching for an item
print(ndila[4])

for p in ndila:# loop items in array that has been created.
	print (p) 
	
# to access an item in python
print (ndila[0])