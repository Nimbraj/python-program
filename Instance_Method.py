#
# # Instance method
#  ### instance  ------> Object
#  #### method :- it is class inside function is called as methods
#
#  # instance Method : ---->
#            # A method it will accept first argument of an object address
# # Syntax:-
# #     class class_name:
# #         def Method_Name(Parameter):
# #             # statement
# #     new_object=class_name()
#
#
#   # step1
#
#
# ## Accessing the data through object new_object.method_name()
#
#
# ### Step ----->  2###########
# ## Accessing the data though class_Name
# ## class_name.method_name()
#
#
# class ShowRoom:
#     def tesla(self):
#         print("the Tesla showRoom ")
# x=ShowRoom()
# # x.tesla()
#
#   ##ShowRoom.tesla(x)
#
#      #########step 1
# class ShowRoom:
#     def Tesla(self):
#         car_name="teslax2"
#         color="Black"    ### Local variable
#         price=123121
#         print(f" My car is{car_name} and car color is a {color} this car is price{price}")
# a=ShowRoom()
# a.Tesla()   # through object
# ShowRoom.Tesla(a)  # through object
#

########### step 2
# class ShowRoom:
#     def tesla(self,Car_name,color_name,price):
#         print(f"My car name is {Car_name},this are color is a {color_name} and car price is a around menas {price}")
# x=ShowRoom()
# x.tesla("forchunar","black",12242) # though olbject
# ShowRoom.tesla(x,"Bmw","blue",234)


# ### step 3
#   # Accessing  class _variable though
# class pyspider:
#     mock_date="30/08/2025"
#     tainer_name=("vikas kalal")
#     def data(self):
#         print(f"moke exam date{pyspider.mock_date} and sql tainer name is a{pyspider.tainer_name}")
# p=pyspider()
#
# pyspider.data(p)

### step 3
  # Accessing  class _variable though class_name
# class pyspider:
#     mock_date="30/08/2025"
#     tainer_name=("vikas kalal")
#     def data(self):
#         print(f"moke exam date{pyspider.mock_date} and sql tainer name is a{pyspider.tainer_name}")
# p=pyspider()
# p.data()
#
### step 4
# Accessnig class Variable through object

# class pyspider:
#     mork_date="30/08/2025"
#     Trainer_name="xyz"
#     def Date(self):
#         print(f"mock_exam date is{self.mork_date}")
#         print(f"Trainer name is{self.Trainer_name}")
# e=pyspider()

# ## Modification Through class_name
# pyspider.Trainer_name="dfg"
# e.Date()
#
# # modification through object
# e.Trainer_name="Mayur"
# e.Date()


#step-->6
# class Pyspider:
#     mock_date="30/08/2025"   #class_variable
#     Trainer_Name="xyz"
#     def Data(self):
#         print(f'mock_exam date is {self.mock_date} '
#               f'Trainer name is {self.Trainer_Name}')
# p=Pyspider()
# p.mock_date="29/08/2025"
# Pyspider.Trainer_Name="*" 
#
# p.mock_date="23/34/203"
# p.Data()

## Step 7    #### BMW ####
# class BMW:
#     def car_details(self,car_price,car_color,*args):
#         print(f"my car price is{car_price} and my car color is {car_color} ",
#               f"exta infromation{args}")
# b=BMW()
# b.car_details(1234,'red',"Bmwx")
# BMW.car_details(b,3423,"red","Bmwx2")


#
# class BMW:
#     def car_details(self,car_price,car_color,*args):
#         print(f"My car price is {car_price} nad my car color{car_color}"
#               f"and extra information of the car and in car{args} ")
# b=BMW()
# b.car_details(100,"blue color","BMWX2")
# b.car_details(2000,"read","the any methods object address an be first argument this methods called as instance methods"
#                           "the point is alway object address to Access to type of object can be two type of first is object and second is class name the class used to paranteses object defined ")
