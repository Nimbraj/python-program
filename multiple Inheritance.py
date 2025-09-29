# class Dad:
#     def Agrii_Land(self):
#         print("40 acres")
# class Mom:
#     def Vill(self):
#         print("mom 's villa")
# class chid(Dad,Mom):
#     def Education(self):
#         print("Still an studying")
#
# a=chid()
# a.Vill()
# a.Education()
# a.Agrii_Land()
#
#
# class Eduction:
#     def Student(self):
#         print("final _year_student")
#     def Information(self):
#         super().Information()
#
#         print("AL+ml subject")
# class Pyspider:
#     def Python(self):
#         print("AI_ML subject")
#     def Information(self):
#         print("ML_information")
# class Student(Eduction,Pyspider):
#     def Data(self):
#         print("Fee structure is too high.....")
#     def Information(self):
#         super().Information()
#         print("data science information")
# x=Student()
# x.Data()
# x.Python()
# x.Information()


#proper one______> diamond program
# class A:
#     def Display(self):
#         ...
# class B(A):
#     def demo(self):
#         ...
# class c(A):
#     ...
# class D(B,c):
#     def check(self):
#         ...
# d=D()
# d.Display()
# d.demo()
# d.check()


# oop
# to represent real words object ot software worlds
# for storing data in an organized way
# for accessing data in an easy manner.
# for  re-usability  purpose
# for maintainability
# any modification done by class will impact all other object
#
# Any modification done  by object it will not impact to class
# and other object and also object will be


# methods
# In simple words a function inside a class is called as methods

# type of methods
# instance methods
# class methods
# static method

# Python is a general purpose high level  programming language
# python was developed by "Guido van Rossum "
# when it was implement  1989
# when it appered to  the public ---->
#      feb 20th 1991


# #   where we can use python language
# for developing desktop applications
# for developing web application
# for developing games
# for machine learning
# for developing Artificial intelligence application


# features of python
# Simple and easy to learn
# the Syntaxes are very simple and easy.
# High level programming language
# freeware and open source
# Platform indentpaendent
# Dynamically typed
# IT support cross  platform
# It sppuort Dynamic memory Allocaton

# python variable
# A variable a name given to a memory location which holds the actual value


##  Memory management in variable

#
#
# num= int(input("Enter a number   "))
# fact =1
# for i in range(1,num+1):
#     fact *=i
# print(f"factorial of{num } is {fact}")

# n=int(input("Enter number of terms: "))
# a=0
# b=1
# print("fibona")

# class customer:
#     def Name(self,last_name,first_name):
#         print(f" this coustomer first name is{last_name}and last name is are {first_name}")
#     def __init__(self,P_name,P_date):
#         print(f"the product name is{P_name} and date of product{P_date}")
# class customer2(customer):
#     def Name(self, last_name, first_name):
#         super().Name("Jagtap","Nimbraj")
#         print(f" this coustomer first name is{last_name}and last name is are {first_name}")
#
#     def __init__(self, P_name, P_date):
#         super().__init__("chican","1242")
#         print(f"the product name is{P_name} and date of product{P_date}")
# e=customer2("mayur",'67/09')
# e.Name("Avinash","tadge")


#
# class A:
#     def spam(self):
#         print("first class")
# class B(A):
#     def demo(self):
#         print("Second Class")
# class C(A):
#     def display(self):
#         print("third class")
# class D(B,C):
#     def Hi(self):
#         print("4th class")
# a=D()
# a.Hi()
# a.spam()
# a.display()
# a.demo()


# class A:
#     def spam(self,x):
#         print("First class",x)
# class B(A):
#     def demo(self,y):
#         print("second class",y)
# class C(A):
#     def Dispaly(self,z):
#         print("Third class",z)
# class D (B,C):
#     def Hi(self,d):
#         print("4th class")
# a=D()
# a.Hi(100)
# a.demo(232)
# a.spam(543)
# a.Dispaly(1232)

# class Parent:
#     def __init__(self):
#         print("its a constructor class")
# class Dad(Parent):
#     def __init__(self):
#        super().__init__()
#        print("Dad class")
# class MoM(Parent):
#     def __init__(self):
#         super().__init__()
#         print("mom class")
#
# class child(Dad,MoM):
#     def __init__(self):
#         super().__init__()
#         print("Child class")
# c=child()
#
# class Bank:
#     def __init__(self, Account_name, Bank_name):
#         self.A = Account_name
#         self.B = Bank_name
#
#     def Data(self):
#         print(f"Account holder name is{self.A}and my bank name is{self.B}")
#
#
# class ATM(Bank):
#     def __init__(self, bal, pin):
#         super().__init__("iCIC123432","pfc123454")
#         self.b = bal
#         self.p = pin
#
#
#     def Data(self):
#         super().Data()
#         print(f"this Account balance {self.b}and pin code this branch{self.p}")
#
#
# class ICIC(Bank):
#     def __init__(self, acc_num, ifcs_code):
#         super().__init__("Mayur Saluke","HDFC")
#         self.num = acc_num
#         self.code = ifcs_code
#
#     def Data(self):
#         super().Data()
#         print(f"this preson account NUmber is{self.num}and ifsc{self.code}")
# class Customer(ATM,ICIC):
#     def __init__(self,loc,branch):
#         super().__init__(1233,413205)
#         self.br=branch
#         self.l=loc
#     def Data(self):
#         super().Data()
#         print(f"the branch in{self.br}and location in {self.l} ")
# C=Customer("pune","ICIC")
# C.Data()
#
# class Student:
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def student_Data(self):
#         print(f"Student name is {self.name}and total score {self.score}")
# class Pyspider:
#     def __init__(self,free, cource_name):
#         s=Student("Mayur Kachru saluke","*")
#         s.student_Data()
#         self.f=free
#         self.c=cource_name
#     def information(self):
#         print(f"total free is {self.f}and cource_name is {self.c}")
# p=Pyspider(11111,"DA/ML/AL")
# p.information()
