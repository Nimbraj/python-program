# ABSTRACTION
# Hiding the compexity of a features and displaing only the
# the required property to the end_user is called as abstraction



# Abstraction methods
# sometimes we don't know about implementation still  we can
# declare .such type of methods are abstraction methods

#abstract methods has only declaration but not implemention
# In python we can declare abstract method by using @abstractionmethods decorator


# Abstract class
# some  time implementation of a class is not complete, such type of partially
# implementation classes are called Abstraction class
# Every Abstract class in python derived from ABC class present in abc Module.


# case--1
from abc import ABC,abstractmethod
# class test:
#     def display(self):
#         print("Display method")
# t=test()
# t.display()

## Case----2
# class test(ABC):
#     def display(self):
#         print("display methods")
# t=test()
# t.display()

# case---3

# class test:
#     @abstractmethod
#     def display(self):
#         print("display methods")
# t=test()
# t.display()

#
# class test(ABC):
#     @abstractmethod
#     def spam(self):
#         pass
# t=test()
#
#
# from abc import ABC,abstractmethod
# class Test():
#     @abstractmethod
#     def First_mock(self):
#         pass
#     @abstractmethod
#     def Second_mock(self):
#         pass
#     def Mock_taken_by(self):
#         pass
# class Data(Test):
#     def First_mock(self):
#         print("I am taking first mock for sql subject")
#     def Second_mock(self):
#         print("I am tacking mock for python ")
#
#     def Mock_taken_by(self):
#         print("the mock taken by python trainers")
# d=Data()
# d.First_mock()
# d.Second_mock()
# d.Mock_taken_by()
#
from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def first_test(self,name,):
        pass
    def mock_ranking(self,rank):
        pass
    def mock_taken_by(self,t_name,subject):
        pass
class Data(Test):
    def first_test(self,name,):
        print(f"the student name is {name}")
    def mock_ranking(self,rank):
        print(f"the student rank  -->{rank}")
    def mock_taken_by(self,t_name,subject):
        print(f"the techar name is {t_name} and subject name are {subject}")
D=Data()
D.first_test("Nimbraj")
D.mock_ranking("*")
D.mock_taken_by("xyz","python")



#
#
#
#
# from abc import ABC,abstractmethod
# class Bank(ABC): #Parent class
#     @abstractmethod
#     def balance(self):
#         pass
#     @abstractmethod
#     def deposit(self,amount):
#         pass
#     @abstractmethod
#     def withdrawal(self,amount):
#         pass
# class ATM(Bank):
#     def __init__(self,bank_name,Account_holder,balance):
#         self.name=bank_name
#         self.holder=Account_holder
#         self.bal=balance
#     def balance(self):
#         print(f" my bank name is {self.name} "
#               f"and account holder name is{self.holder}"
#               f"and Total balance is {self.bal}")
#     def deposit(self,amount):
#         self.bal +=amount
#         print(f"before deposit total amount is{self.bal}")
#         self.bal+=amount
#         print(f"after deposit total amount is {self.bal}")
#     def withdrawal(self,amount):
#         self.bal-=amount
#         print(f"after withdrawal total balance is{self.bal}")
# a=ATM("ICICI","Kiran",1000)
# a.balance()
# a.deposit(5000)
# a.withdrawal(2500)
#






# from abc import ABC,abstractmethod
#
# class Bank(ABC):
#     @abstractmethod
#     def information(self,name,address):
#         print('Bye')
#
# class ICIC(Bank):
#     def information(self,name,address,Account_number):
#         super().information(name,address)
#         print(f"the one preson details is   {name} and address   {address} this is a Account number   {Account_number}")
# obj=ICIC()
# obj.information("mayur","pune","ICIC1236432")
#
#
#
#
#


class Method:
    def __int__(self ,name,number):
        self._n=name
        self.num=number
    def getter(self):
        return self._n ,self.num
    def setter(self, name,number):
        self.num=number
        self._n=name

    def deletter(self):
        del self.num ,self._n
obj=Method()
obj.setter("mayur",123)
print(obj.getter())


