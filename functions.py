#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:32:07 2019

@author: hala
"""
import functools

#Q1
o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))

#2=


list1=[2,3,5,4,3]
def multi(list1):
    multip=1
    for item in list1:   
        multip=item*multip
    return multip   
print(multi(list1))  
#Q3
multi = lambda a, b : a * b
print(multi(5, 6))
#Q4
number_list=range(-5,5)
negative=list(filter(lambda x: (x < 0), number_list))
print(negative)

#Q5
x=lambda a,b,c :a+b+c
print(x(5,6,2))

#Q6    
x = ("Joey","Monica","Rose")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")
result=list(zip(x,y,z))
print (result)
 
#Q7
coin=("Bitcoin","Ether","Ripple","Litecoin")
code=("BTC","ETH","XRP","LTC")
d= dict(zip(coin,code))
print(d)

#Q8
def fun(variable):
    letters =["a","e","i","o","u"]
    if (variable in letters):
        return True
    else:
        return False
sequence=["g","j","e","j","k","o","p","r"]
filtered = list(filter(fun,sequence))
print (filtered)    

#Q9
x=list(map(int,input("Enter a multiple value: ").split()))
print("List of students: ",x)

#Q10
def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)
#Q11
def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
#Q12
c= map(lambda x:x+x,filter(lambda x:( x >= 3),(1,2,3,4)))
print(list(c))

#Q13
c=filter(lambda x:(x >= 3),map(lambda x:x+x,(1,2,3,4)))
print (list(c))

#Q14
list2 = [1,-2,-5,-7,3,5,6,2]
min=functools.reduce(lambda a,b : a if a<b else b,list2)
print(min)
#Q15
numbers=[1,2,3]
letters=["a","b","c"]
convert=tuple(zip(numbers,letters))
print(convert)


