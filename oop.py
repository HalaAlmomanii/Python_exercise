#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:52:14 2019

@author: hala
"""




class Employee:
    def __init__(self,number:int,name:str,address:str,salary:float,job:str):
        self.number=number
        self.__name=name
        self.__address=address
        self.__salary=salary
        self.__job=job
        
    def getname(self):
        return self.__name
    def getaddress(self):
         return self.__address
    def getsalary (self):
        return self.__salary
    def getjob(self):
        return self.__job
        
    def setaddress(self,myaddress):
        self.__address=myaddress
        
    def __del__(self):
            print(self.__name+" has been remove")
    def func1(self):
        print("number =",self.number,"name=",self.__name,"addres=",self.__address,"job=",self.__job)
    def func2(self):
        print("number =",self.number)
        print("name=",self.__name)
        print("addres=",self.__address)
        print("job=",self.__job)

Employee1=Employee(1,"Hala","USA",500,"consultant")
Employee2=Employee(2,"Rana","JOR",300,"manger")

Employee1.func1()
Employee1.func2()

Employee2.func1()
Employee2.func2()

Employee1.setaddress("SYR")

print(Employee1.getaddress())

Employee1.func1()

del Employee1
del Employee2