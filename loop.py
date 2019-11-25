#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:40:01 2019

@author: hala


name=input("enter your name ")
age=int(input("enter your age "))

if age <18:
    print("you are under age")
    avg=int(input("enter your avg  "))
    if (avg>=90):
        print("above 90")
    elif(avg>=50):
        print("passed")
    else:
        print("failed")

else:
   print("adult")
   title=input("enter your title")
   print(title,age,name)
   




z=1
x=1
y=9
while x<9:
    while z < y:
        print(" ",end="")
        z+=1
    print ("*"*x)
    x+=1
    z=1
    y-=1
    
   _________________________________________________________________________________________________ 
    
Q1
x=int(input("enter first number"))
y=int(input("enter sec number"))
print(x) if x>y else print(y)

Q2
x=int(input("enter yor number"))
for i in range(1,11):
  print(x,"*",i,"=",x*i)
  
  Q3
  x=0
while x<=5:
 print("*"*x)
 x+=1
z=4
while z>=1:
 print("*"*z)
 z-=1
 
 Q4
 letters=["x","y","z","a","b","c"]
for i in letters:
    if i=="a":
     continue
    elif i=="c":
      break
    print(i)
    
 Q5
    for x in range(12,25,3):
        print(x)
    
Q6
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
Q7
result=0
x=int(input("enter number"))
for i in range(0,x+1):
    result=result+i
print("the avg from 0 to",x,"is",result/x)

Q8
x=int(input("enter number"))
print("even") if x%2==0 else print("odd")

Q9
hala=9
for x in range(1,10):
    for y in range (1,hala):
        print(" ",end=" ")

    for z in range (1, x):
        print(z,end=" ")
    hala-=1
    
    for w in range(x,0,-1) :
        print(w,end=" ")
    
    print("")



k=1
for x in range(8,0,-1):
    for y in range (0,k):
        print(" ",end=" ")

    for z in range (1,x):
        print(z,end=" ")

    
    for w in range(x,0,-1) :
        print(w,end=" ")
        
    
    print("")
    
    k+=1


 
Q10
while True :
    try:
        x=int(input("please enter integer number:"))
        break
    except ValueError:
         print("try again it's not integer")
        
print("thank you")

Q11
try:
    a=3
    if a<4:
       b=a/(a-3)
       print(b)
except (ZeroDivisionError,NameError):
    print(" it's Error")
"""





    
    
 

    
   
    








