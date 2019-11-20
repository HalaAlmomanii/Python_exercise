# -*- coding: utf-8 -*-

"""
Q1
print("Hello \n %9s  \n %14s "%  ("Hello","Hello"))
 Q2
print("Orange academy \n" *20 )

Q3
x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x,y,z,sep='10')


Q4
x,y=input("enter your  values" ).split(",")
x=int(x)
y=int(y)
print ("your oproduct is", x*y)

Q5
avg=eval(input("enter five numbers"))
result=0
for x in avg:
    result=result+x
print (result/5)

Q6
x=1
y=2.8
z=1j
o="orange"
A=True
print(type(x),type(y),type(z),type(o),type(A))


Q7
str1,str2="Hala",1
str3,str4=100,-1
print(str1,str2,str3,str4)



Q8
x=10
print(x)
x_Q="orange"
print(x_Q)
AB=10
print(AB)
print("10"*10)


Q11

#Print("Hala")
print("this is output") #print("done")

Q12
name,age=input("enter your name and age").split(",")
age=int(age)
div=100-age
print("Hello" ,name, "at ",2019+div,"Years to turn 100")

Q13

base, h= input ("enter base and h of tringale").split(",")
print("the Area is", int(base)*int(h)*.5)
"""
def greet(name,time):
 print(f'Good {time} {name}, hope u are well')
 
name,time=input("enter you name? and time with comma").split(",")
greet(name,time)
