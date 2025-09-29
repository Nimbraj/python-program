# by using className or by creating object we can access member of one class inside
#     Another class is nothing but composition

# the advantages of Has-a-relationship os code reusability.
#
# class Engine:
#     a=10
#     def __init__(self):
#         print("its python class")
#     def m1(self):
#         print("Day wasted Guys")
# class Car:
#
#     def __init__(self):
#         self.engine=Engine()
#         print(self.engine.a)
#         print("hey guys super")
#         print(self.engine.m1())
#     def M2(self):
#         print("its cool")
# C=Car()


# class Hero:
#     def spam(self):
#         print("evening class ")
# class Queen:
#     def demo(self):
#         print("Afternoon")
#         a=Hero()
#         a.spam()
# b=Queen()
# b.demo()


# class Test:
#     name="python"
#     def spam(self):
#         print("spam method")
# class Sample:
#     def demo(self):
#         print("demo methods")
#         a=Test()
#         print(a.name)
#         a.spam()
# b=Sample()
# b.demo()



# class Car:
#     loc="pune"
#     def __init__(self):
#         print("Car class")
#     def M1(self):
#         print("M1 class")
# class Car2:
#     def __init__(self):
#         print("constructor class")
#         self.y=Car()
#         print(self.y.loc)
# x=Car2()


#
#
# class Qspider:
#     def __init__(self,name,batch_code,room_number):
#         self.name=name
#         self.batch_c=batch_code
#         self.room_N=room_number
#     def Student_details(self):
#         print(f"Qspider student name is{self.name}"
#               f"and he attending"
#               f"class batch code is{self.batch_c}"
#               f"and room number is{self.room_N}")
# class Pyspider:
#
#     def __init__(self,subject,fee,student_count):
#         self.Q=Qspider("Rahul","m3",2)
#         self.subject=subject
#         self.fee=fee
#         self.student_count=student_count
#         self.Q.Student_details()
#     def Student(self):
#         print(f"Pyspider student subject is{self.subject}"
#               f"and total free is{self.fee} and total"
#               f"student strength{self.student_count}")
# p=Pyspider("Python",30000,25)
# p.Student()


