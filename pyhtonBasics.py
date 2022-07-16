x=1.0067
istrue=True #case sensitive
print(istrue)
name="chandana"
print("name")
print(x)
print("Hello world")

#y=input("what is your name?")
#str(y) by default input is string#print("Hello"+5) -- error strings
name.upper() #method
print(name)
print(int(x)); #type conversion
print(name.find('a'))
#case sensitive character and string.
print(name.replace("ana","chan"))
#if exists
print("chan" in name)
#returns bool value
print(5//2) #removes after decimal digits
print(2**5) #power

#block of statements using if else

age=10
if age >=10: #statement
    print("you are in block")
    print("you're still in block due to indentation")
elif age<10 and age>3:
    print("in else if")
else:
    print("last one")
print("out of block")
#range
print(range(5)) #0,1,2,3,4 (5 not included!)
v=1
while v<=5:
    print(v)
    v+=1
h=range(5)
for i in range(5):
    print(i)
#lists: collection of items
marks=[98,76,14]
print(marks)
marks=[1,5,"nulli"] #also supports different data types
print(marks[0])
print(marks[-1]) #-1 in python is from end. end= -1
print(marks[0:2]) #from 0 to 2(2 not included)
for score in marks:
    print(score)
#operations in lists
marks.append(99)
print(marks)
marks.insert(0,99) #insert at 0th position
print(99 in marks)#if exists
print(len(marks))
i=0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()
print(marks)
#tuple
#similar to list, not mutable or chngeable
marks=(99,9898,67,14)
marks[0]=99 #error
#(by default tuples)operations on tuple
print(marks.count(98))
print(marks.index(98))
#set 
marks={98,98,98}
print(marks[0]) #cant access by index
for i in marks:
    print(i)
#by default sets are unordered since no index
#dictionary: key-value pairs
marks={"eng":98,"social":90}
print(marks["eng"])
#add
marks["phy"]=98
#functions
#inbuilt,module,userdefined
#module: import math print(dir(math))
#from math import *
def fun(x,y=9):
    x=x*7
    print(x)
    print(y)
fun(78)
fun(78,9)


