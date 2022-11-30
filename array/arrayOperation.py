from array import *

arr1 = array('i',[10,30,50,70,90])
for x in arr1:
    print(x)
    
#Insertion Operation
arr1.insert(2,20)
for x in arr1:
    print(x)

#Deletion Operation
arr1.remove(90)
for x in arr1:
    print(x)

#Search Operation
print(arr1.index(30))
for x in arr1:
    print(x)
    
#Update Operation
arr1[4]=100
for x in arr1:
    print(x)