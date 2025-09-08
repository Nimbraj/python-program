# class Dad:
#     loan="2cr"
#     def villa(self):
#         print("20 floor villa")
# class Child:
#     bike="BMW"
#     def joy(self):
#         print("injoy")
# c=Child()
# C=Dad()
# C.villa()
# c.joy()
# print(dir(Dad))
# print()
# print(dir(Child))
#
#
#
# # step ---1
# class Bike:
#     def Dream(self,bike_price,color):
#         print(f'my bike total price is {bike_price} and bike color is {color}')
# class ShowRoom(Bike):
#     def Bike_information(self):
#         print("My bike is a bmw x3")
# s=ShowRoom()
# s.Bike_information()
# s.Dream(3345335,"black")
#
#
# # step----2
# class Test:
#     def demo(self):
#         print("demo mMethod")
#     def spam(self):
#         print("Test---> class")
# class T(Test):
#
#     def demo(self):
#         print("T---> class")
#         super().spam()
#         print("spam methood is a 2")
# t=T()
# t.demo()
# t.spam()
#
#   # step ---3
# class Data:
#     def __init__(self):
#         print("Constructor Class--->1")
#     def display(self):
#         print("Data class")
# class Information(Data):
#     def __init__(self):
#         super().__init__()
#         print("infromation class")
#     def Dream(self):
#          print("deram class")
# w=Information()
# w.Dream()
# w.display()
#
#
#               ##### step 4
# class Flipkart:
#     def __init__(self,price,location):
#         print(f"total of item is{price} and location is {location}")
# class Ekwart(Flipkart):
#     def __init__(self, name,total_price):
#         super().__init__(1312,"Mumbai")
#         print(f"product name is a{name} and total price is{total_price}")
#
# f=Ekwart("Jagtap Nimbraj",123432)
# #
#
# ##################################
# class Bike:
#     def Dream(self,bike_price,color):
#         print(f"my bike total price is a {bike_price}")
# class ShowRoom(Bike):
#     def Bike_information(self):
#         print("My bike name is a--->x2")
#     def Dream(self,bike_price,location ,color):
#         super().Dream(1234321,"blue ")
#         # super().Dream(bike_price=1232,color="black")
#         # super().Dream(bike_price,color)               thread way is a---#
#         print(f"show room location is {location}")
# s=ShowRoom()
# s.Bike_information()
# s.Dream(111,"Blue","Deccan")


class Pyspider:
    def __init__(self,std_name,mock,sid):
        self.n=std_name
        self.m=mock
        self.s=sid
    def Student_information(self):
        print(f"My student name is {self.n} "
              f"and mock rating is {self.m}"
              f"Student id is {self.s}")
    def Python(self):
        print("Full-Stack python subject")
class Qspider(Pyspider):
    def __init__(self,batch_code,timing,room_number):
        super().__init__("Mayur saluke","*","std131")
        self.B=batch_code
        self.t=timing
        self.r=room_number
    def Student_information(self):
        super().Student_information()
        print(f"Python subject batch code is{self.B}"
              f"and timing of class {self.t}"
              f"python subject class room is{self.r}")
    def Python(self):
        super().Python()
        print("Data Analysis Subject is python languages")
x=Qspider("e3","5-4","Room-->4")
x.Student_information()
x.Python()
#
#
# class College:
#     def __init__(self,C_name,C_Address,C_depatement):
#         self.n=C_name
#         self.A=C_Address
#         self.D=C_depatement
#     def College_information(self):
#         print(f"the you college name is {self.n} and"
#               f"this Address of a{self.A}"
#               f"and this type of depatement  is{self.D}")
#     def Worknig(self):
#         print("the woorking is a multiple working is a college")
# class  depatement(College):
#     def __init__(self,d_name,d_fooler,d_timing):
#         super().__init__()
#         self.d=d_name
#         self.f=d_fooler
#         self.t=d_timing
#     def De_infrormation(self):
#         print(f"the working is {self.d}"
#               f"and this fooler {self.f}"
