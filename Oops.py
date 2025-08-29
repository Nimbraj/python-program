# # How to create empty class
# class className:
#     ...
#
# class clasName:
#     pass

## How to create object
#New_var_name=className()
# ...

# class test:
#     ...
# t=test()

# class ClassName:
#     classvariable
#     method
#     constructor
# object=ClassName()


# class variable ---> Any variable it will present inside the class that type variable
# we can call it as a class variable

class Employee:
    name="Avii"
    eid="A123"
    sal=25000
e=Employee()
print(e.name)
print(e.eid)
print(e.sal)

# Class_infromation-->
# Class_name---> Employee
# object_name--> e
# class_variable---->name,eid,sal

# class variable we are access outside directly(it will won't work)
#print(name)  NameError: name 'name' is not defined
#print(eid)   NameError: name 'name' is not defined
#print(sal)  NameError: name 'name' is not defined
# step1
# class_variable am accessing outside by using object
# print(e.name)
# print(e.name)
# print(e.sal)
# step2
# print(Employee.name)
# print(Employee.eid)
# print(Employee.sal)


#  ####Note-->if we want access class variable outside
# here we have two way
#         1.by using ClassName
#         2.by using object


#     ###   What is the difference between with --() and without --->()
# e.Employee()
print(e) #<__main__Employee object at eskdm23245fdq343>



class ShowRoom:      #class name--->ShowRoom
    name='Testa'      ##class_variable
    color='Red'       ##class_variable
    price=50000       ##class_variable
s=ShowRoom()
# To access class_variable outside by using class_name
print(ShowRoom.name)
print(ShowRoom.price)
print(ShowRoom.color)

# TO access class_variable outside by using object_name
print(s.name)
print(s.color)
print(s.price)



#########
 ## internally all the data will be present in the form of key and value pair

 #---> Class_name.__dict__
 # print(ShowRoom.__dict__)


#


class Emp:
      '"Employee infromation"'
      sal=100
      age=14
r=Emp()
r1=Emp()
print(Emp.__dict__)
help(Emp)
# print("Before modification in class---> ")
# print(Emp.sal)
# print(r.sal)
# print(r1.sal)
r1.sal=2345
print("without modification output in e-->object")
print(Emp.sal)
print(r1.sal)
print(r.sal)


#            Point----> 1
# ---------------------------------------------------------------
# if we done any modification in main class it will
#     effect for both object


              # Point --->2
# if we done any modification ni any one object
# it will won't effect to main class
# as well as other object


   ###      Point
# # agin if we done any modification in class it will effect
# # for main class and other object. but it will won't
# # ' effect for previous object
# because whe we done modification in
# object we are losing the connection
# #