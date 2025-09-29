############# Encapsulation ########
# Encapsulation refers to the binding of data and
# code together into single unite  is called as encapsulation


# declaring a member of
# class with private and restrict the access outside the class provide the class indirectly by sing getter  setters
# is called encapsulation

# in python we can' achieve 100% encapsulation
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
# any member which is starting/perfixed
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

class College:
    def __init__(self,name,Address):
        self._name=name
        self._add=Address
    def getter(self):
        return self._name,self._add
    def setter(self,name,add):
        self._name=name
        self._add=add
    def dellter(self):
        del self._add ,self._name
c=College("Dr Dy Patil ACS  College ","pimpri")
print(c.getter())
print(c.setter("modren college pune","pune"))
print(c.getter())
print(c.dellter())
print(c.getter())