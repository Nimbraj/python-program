############# Encapsulation ########
# Encapsulation refers to the binding of data and
# code together into single unite  is called as encapsulation
# dunder unit another name of constructor also called __init__()
# -->static method is use  to perform independent operation
# constructor is used initialize the object member or instance variable.
# @ property `  ---> this property use for declaring the geter , seter and deliter method
#what is inheritance what are the types of inheritance
from abc import abstractmethod
#
# the method having only  declaration but no body/defination.                              before the declaration
# in class is single method is present abstract is called abstractclass
# concreat class --> a normal class (a method present with defination and declaration )
#
# how to create  abstractmethod+
# from abc import ABC,abstractmethod
# class demo()

# declaring a member of
`
















































































































# class with private and restrict the access outside the class provide the class indirectly by sing getter  setters
# is called encapsulation

# in python we can't achieve 100% encapsulation
# in the python we have 3 access specifier

# public
# private
# Protected
# public access specifier:-
#   Any member (variable /method ) without any
#   perfix(_) the it is called as public specifier


# ex:- var_name,def add()
# class Employee:
#     def __init__(self,name,pay):
#         self.name=name
#         self.pay=pay
#     def disp(self):
#         print(f" in display in employee class {self.name} and salary is pay in per month {self.pay}....")
#
# E=Employee("sukshala",23321)
# E.disp()
#



# 2.Protected access specifier
# any member which is starting/prefix
# with single underscore(_) then it is called as protected
# class Emp:
#     _pin=2312
#     def _disp(self):
#         print("the in display")
#     def getter(self):
#         return self._pin
#     def setter(self,pin):
#         self._pin=pin
# e=Emp()
# pin=e.getter()
# print(e.getter())
# pin=e.setter(22222)
# print(pin)
# pin=e.getter()
# print(pin)

# class College:
#     def __init__(self,name,Address):
#         self._name=name
#         self._add=Address
#     def getter(self):
#         return self._name,self._add
#     def setter(self,name,add):
#         self._name=name
#         self._add=add
#     def dellter(self):
#         del self._add ,self._name
# c=College("Dr Dy Patil ACS  College ","pimpri")
# print(c.getter())
# print(c.setter("modren college pune","pune"))
# print(c.getter())
# print(c.dellter())
# print(c.getter())

# Protected Access specifiers
# class Bank:
#     _pin=123
#     def _dispaly(self):
#         print("Bank information")
#         print(self._pin)
#         print(self._pin)
# b=Bank()
# b._pin=111
# print(b._pin)
# b._display()


 ################
# class ATM:
#     def __init__(self,pin):
#         self._pin=pin
#
#     def getter(self):
#         return (self._pin)
#     def setter(self,pin ):
#         self._pin=pin
#     def Deleter(self):
#         del self._pin
# a=ATM(123)
# a.getter()
# print(a.getter())
# a.setter(457)
# print(a.getter())
# a.Deleter()
# print(a.getter())
# ###########
# class Student:
#     def __init__(self,name,subject):
#         self._name=name
#         self._sub=subject
#     def getter(self):
#         return self._name,self._sub
#     def setter(self,name, sub):
#         self._name=name
#         self._sub=sub
#     def Deletter(self):`
#         del self._name
#         del self._sub
# c=Student("ABC","python")
# c.getter()
# print(c.getter())
# c.setter("XYZ","REACT.JS")
# print(c.getter())
# c.Deletter()
# print(c.getter())


## Private Access specifiers
# class Demo:
#     __name="python"
#     def spam(self):
#         print(f"my name is{self.__name}")
# d=Demo()
# d.spam()
# # print(d.Demo_name)
# # print(Demo.Demo_name)
#
# class Account_Details:
#     def __init__(self,bank_name,Account_number,balance):
#         self.bank=bank_name
#         self._acc=Account_number
#         self.__bal=balance
#     def getter(self):
#         return self.bank,self._acc,self._acc,self.__bal
#     def setter(self,bank_name, acc_num,bal):
#         self.bank=bank_name
#         self._acc=acc_num
#         self.__bal=bal
#     def diletter(self):
#         del self.__bal,self._acc,self.bank
# a=Account_Details("ICIC","ICIC12264246",670000)
# print(a.getter())
# a.setter("SBI","SBI123452",903411)
# print(a.getter())
# a.diletter()
# print(a.getter())


#
# class Information:
#     def __init__(self,c_name,location):
#         self.name=c_name
#         self.loc=location
#     @property
#     def Data(self):
#         return self.name,self.loc
#     @Data.setter
#     def Data(self,name):
#         self.name=name
#         self.loc=location=name
#     @Data.deleter
#     def Data(self):
#         del self.loc,self.name
# c=Information("azx","Nagar")
# print(c.Data)
# c.Data=("py","Deccan")
# print(c.Data)
# # del c.Data
# # print(c.Data)
