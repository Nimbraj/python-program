from json import JSONEncoder
from random import sample
from symtable import Class

## Adding element to a dictionary
# 1.key - value syntax
# 2.update
#3. set default
#4.from keys
            ##### 1. key -value syntax
            # dict[new key]= value
# fam ={ "davanagere":"glass house","mysore":"palace"}
# fam["jaipur"]="hawa mahal"
# print(fam)
#
#
# # ####update#########
# #     syntax:
# #        dict.update({key:value})
# # update examples
# a={1:2}
# a.update({"a":9})
# print(a)
# p={"banglore":57001,"kalaburagi":4334 ,"jaipur":302001 }
# p.setdefault("dawanagere",577004)
# p.setdefault("Nannaj",413205)
# p.setdefault("deccan")
#
# print(p)
#
# #4. fromkeys():
# a="hello"
# print(dict.fromkeys(a))
#
#
#  # removing elements from A dictionary
#  # pop()
#
#
# ## count frequency of element
# arr=[1,2,1,2,3,1,2]
# freq=()


# arr=[1,2,2,3,1,1,4,2,]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)
#  swap key and value
# d={'a':1,'b':2,'c':3}
# swaped={v:k for k ,v  in d.items()}
# print(swaped)



# # checked if two dictionary are equal
# d1={'a':1,'b':2}
# d2={'b':2,'a':1}
# print(d1==d2)
       # # Merge two dictonaries and value
# d1={'a':10,'b':20,'c':30}
# d2={'a':40,'b':40,'d':60}
# merged=d1.copy()
# for k,v in d2.items():
#     merged[k]=merged(k,0)+v
# print(merged)

#
# # find key with maximum value
# d={'a':100,'b':200,"c":50}
# max_key=max(d,key=d.get())
# print(max_key)
#
#
# # revome the duplicate value
# d={'a':1,'b':2,'c':1,'d':3}
# unique={}
# for k,v in d.items():
#     if v not in unique.values():
#         unique[k]=v
# print(unique)
#

 # Group words by first letter
# words=['apple','banana','apricot','cherry','blueberry']
# grouped={}
# for word in words:
#     first = word[0]
#     grouped.setdefault(first.append(word))
# print(grouped)

 # sort dictionary by value
d={'a':3,'b':1,'c':2}
asc=dict(sorted(d.items(),key=lambda x:x[1]))
des=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print("Ascending:",asc)
print("descending :",des)





# convert two list into dictionary (ignore duplicate)
# keys=['a','b','c','d','a']
# value=[1,2,3,45,]
# d={}
# for k,v in zip (keys ,value):
#     if k not in d:
#         d[k]=v
# print(d)

# fatten nested dictonary
# def fatten(d,p_key=,spe=):
# d1={"a":1,'b':2,'c':3,"d":4}
# d2={'b':10,'c':20,'e':30,"f":40}
# m= d1.copy()
# for k ,v in d2.items():
#     m[k]=m.get(k,0)+v
# print(m)
# class Library:
#     def __init__(self):
#         self.book={}
#     def add_book(self, name ,price):
#         if name in self.book:
#             print(f"{name} is already present in the library ")
#         else:
#             self.book[name]=price
#             print(f"Book {name} added with price {price}.")
#     def update_price( self, name, price):
#         if name in self.book:
#             print(f"price of {name} update to price{price}")
#         else:
#             print(f"{name} is  not available in the library")
#     def display_book(self):
#         """Display all book with price"""
#         if not self.book:
#             print("no book in the library")
#         else:
#             print("Book in the library :")
#             for name ,price in self.book.items():
#                 print(f"{name}: Rs{price}")
# Lab=Library()
# Lab.add_book("Python Basics",300)
# Lab.add_book("Data Structures",450)
# Lab.add_book("Python Basics",300)
# Lab.update_price("Data Structures",500)
# Lab.update_price("Machine Learning",800)
# Lab.display_book()

# Create a Python class Subscribe to maintain
# subscriber counts for each hour of the day. Use a
# dictionary where: Key = Hour (e.g., 1, 2, 3 …)
# Value = Number of subscribers at that hour. The
# class should have the following methods:
#     1. add_hour(hour, subscribers) If the hour is
#     not present, add it with the given number of
#     subscribers. If the hour is already present,
#     update it by adding the new subscribers to the
#     existing subscribers.
#     2. total_subscribers() Display the total number of subscribers across all hours
#     . 3. subscribers_in_hour(hour) Display the number of subscribers for a particular hour.
#     If the hour
# is not present, display an appropriate message.
#
# class Subscribe:
#     def __init__(self):
#         self.subscribres={}
#         # dictionary to maintain hour: subscriber_count
#
#     def add_hour(self,subscribes,hour):
#         if hour in self.subscribres:
#             self.subscribres[hour]+=subscribes
#         else:
#             self.subscribres[hour]=subscribes
#
#     def total_subscribers(self):
#         return sum(self.subscribres.values())
#     def subscribers_in_hour(self,hour):
#         if hour in self.subscribres:
#             return f"subscrible in hour{hour}:{self.subscribres[hour]}"
#         else:
#             return f"No data available for hour{hour}"
# A=Subscribe()
# A.add_hour(1,50)
# A.add_hour(2,30)
# A.add_hour(1,20)
#
# print("Total subscribers : ",A.total_subscribers())
# print(A.subscribers_in_hour(1))
# print(A.subscribers_in_hour(3))
#


#
# Write a Python program to reverse a given number. While reversing,
# if any digit is 0, replace it with 5. Do not use string operations.
# Example Input/Output: Input: 1020 Output: 5201 Input: 8090 Output: 5908
#
# def reverse_replace(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         if digit ==0:
#             digit = 5
#         rev =rev * 10 +digit
#         num //=10
#     return rev
# num= int(input("Enter a number:  "))
# print("Output : ", reverse_replace(num))


####################################
# Create a Python program using inheritance in the banking domain with the following requirements:
#
# Create a base class BankAccount with:
#
# Attributes: account_number, holder_name, balance.
#
# Methods:
#
# deposit(amount) → Add money to the account.
#
# withdraw(amount) → Deduct money if sufficient balance exists, otherwise display "Insufficient balance".
#
# display() → Display account details.
#
# Create a derived class SavingsAccount that inherits from BankAccount with:
#
# Additional attribute: interest_rate.
#
# Method: add_interest() → Calculate and add interest to balance.
#
# Create another derived class CurrentAccount that inherits from BankAccount with:
#
# Additional attribute: overdraft_limit.
#
# Override the withdraw() method → Allow withdrawals even if balance is less than the amount, but only up to the overdraft limit. If exceeded, display "Overdraft limit exceeded!".
#
# Write a program to demonstrate the functionality by:
#
# Creating a SavingsAccount object, depositing money, adding interest, and displaying details.
#
# Creating a CurrentAccount object, performing withdrawals within and beyond the overdraft limit, and displaying details.
# class BankAccount:
#     def __init__(self,account_number,holder_name,balance=0):
#         self.acc_number=account_number
#         self.ho_name=holder_name
#         self.balance= balance
#     def deposit(self,amount):
#         self.balance +=amount
#         print(f"Deposited{amount}. new balance :{self.balance}")
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance -= amount
#             print(f"withdraw {amount}.Remaining balance:{self.balance}")
#
#         else:
#             print(f"Account NO :{self.acc_number} Holder: ",{self.ho_name}  )
#     def  Display(self):
#         print(f"Account no{self.acc_number}"
#               f" and hoder name{self.ho_name}and balance"
#               f" this Account{self.balance}")
# class SavnigAccount(BankAccount):
#     def __init__(self,account_number,Hoder_name,balance=0,interest_rate=5):
#         super().__init__(account_number,Hoder_name,balance)
#         self.interest_rate=interest_rate
#     def add_interest(self):
#         interst=(self.balance*self.interest_rate/100)
#         self.balance +=interst
#         print(f"interest{interst}add new balance :{self.balance}")
# class CurrentAccount(BankAccount):
#     def __init__(self,account_number, hoder_name,balance=0,overdraft_Limit=50):
#         super().__init__(account_number,hoder_name,balance)
#         self.limit=overdraft_Limit
#     def withdraw(self,amount):
#         if amount<=self.balance+self.limit:
#             self.balance -= amount
#             print(f"withdraw{amount}.Remaining balance:{self.balance}")
#         else:
#             print("Overdraft limit exceeded !")
# b=BankAccount("sbi124342","Mayur",100000)
# b.deposit(50000)
# b.withdraw(25000)


# s=Savnifv gAccount("sbi123322","Amit",100000,8)
# s.Display()
# s.deposit(50000)
# s.add_interest()

# C=CurrentAccount("HFD4323432","mayur",100000,30000)
# C.deposit(50000)
# C.withdraw(20000)
# C.Display()


#
# from abc import ABC,abstractmethod
# class CAR(ABC):
#     def __init__(self,brand,price):
#         self._brand=brand
#         self.__price=price
#     def Get_Data(self):
#         return self._brand,self.__price
#     @abstractmethod
#     def type_ful(self):
#         pass
# class Electric_car(CAR):
#     def __init__(self,brand,price,battery_capacity):
#         super().__init__(brand,price)
#         self.battery=battery_capacity
#     def type_ful(self):
#         print(f"the car information{self.Get_Data()} and electric car{self.battery}")
# class Petrol(CAR):
#     def __init__(self,brand,price,petrol_capacity):
#         super().__init__(brand,price)
#         self.ful=petrol_capacity
#     def type_ful(self):
#         print(f"The information {self.Get_Data()} and petrol car {self.ful}")
# e=Electric_car("TATA",1550000,350)
# p=Petrol("Mahindra",1200000,100)
# e.type_ful()
# p.type_ful()
#
# class Employee():
#     def sal_cal(self,sal):
#         print(f"monthly salary is rs{sal},with 100 to total sal rs8500")
# e=Employee()
# # e.sal_cal(100)
# # Employee.sal_cal(e,100)
#
# class Sample:
#     exm_date="23-05-2025"
#     @classmethod
#     def colle1(cls):
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
#
#     @classmethod
#     def colle2(cls):
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
#     @classmethod
#     def collge3(cls):
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
# a=Sample()
# a.colle1()
# a.colle2()
# a.collge3()

#
#
# from abc import ABC,abstractmethod
# class CAR(ABC):
#     def __init__(self ,brand,price):
#         self._brand=brand
#         self.__price=price
#     def Get_data(self):
#         return self._brand,self.__price
#     @abstractmethod
#     def type_ful(self):
#         pass
# class Electric_car(CAR):
#     def __init__(self,brand,price,battery_capacity):
#         super().__init__(brand,price)
#         self.battery=battery_capacity
#     def type_ful(self):
#         print(f"the car infromation {self.Get_data()}and elctric car{self.battery}")
# class Petrol(CAR):
#     def __init__(self,brand,price,petrol_capacity):
#         super().__init__(brand,price)
#         self.ful=petrol_capacity
#     def type_ful(self):
#         print(f"the information {self.Get_data()} nad petrol car{self.ful}")
# e=Electric_car("TaTa",1950000,600)
# p=Petrol("Mahindra",2350000,"100")
#
# p.type_ful()
# e.type_ful()


#
# from abc import ABC,abstractmethod
# class Account(ABC):
#     def __init__(self,Account_number,balance):
#         self._account=Account_number
#         self.__bal=balance
#     def Get_Data(self):
#         return self._account,self.__bal
#     @abstractmethod
#     def Account_type(self):
#         pass
# class Saving_Account(Account):
#     def __init__(self,Account_number,balance,interst_rate):
#         super().__init__(Account_number,balance)
#         self.in_rate=interst_rate
#         self.bal=balance
#         self.bal /=self.in_rate
#     def Account_type(self):
#         print(f"the information about saving Account {self.Get_Data()}and interest rate saving Account {self.in_rate} % final amount{self.bal+self.in_rate}")
# class Current_Account(Account):
#     def __init__(self,Account_number,balance,over_limit):
#         super().__init__(Account_number,balance)
#         self.limit=over_limit
#
#     def Account_type(self):
#         print(f"the information about  Current_Account{self.Get_Data()}and limit of account as{self.limit}")
# s=Saving_Account("SBI1234",500000,7)
# s.Account_type()
# c=Current_Account("ICIC12343",120000,50000)
# c.Account_type()
#




#
# class Iformation:
#     def __init__(self,name,address):
#         self.name=name
#         self.add=address
#     def Get_Data(self):
#         return self.name,self.add
#     def extra_infomation(self,Number,Acc_number):
#         print(f"the are {Number}and Account{Acc_number} ")
# class ICIC(Iformation):
#     def __init__(self,name,address,location):
#         super().__init__(name,address)
#         self.loc=location
# #
# #     def extra_infomation(self,number,Acc_number):
# #         super().extra_infomation(number,Acc_number)
# #         print(f"the information is {self.Get_Data()} ")
# #
# #
# # class SBI(Iformation):
# #     def __init__(self, name, address, location):
# #         super().__init__(name, address)
# #         self.loc = location
# #
# #     def extra_infomation(self, number, Acc_number):
# #         super().extra_infomation(number, Acc_number)
# #         print(f"the information is {self.Get_Data()} ")
# # I=ICIC("jagtap","pune","Deccan")
# # I.extra_infomation(9322700648,"ICIC123432")
# # I=SBI("Ram","Jamkhed","Nagar")
# # I.extra_infomation(345679876543,"sisi123432")
# #
# # # Encapsulation ->
# # hape Drawing App
# #
# # You are building a drawing app. You have classes Circle, Square, and Triangle.
# #
# # Each has a method draw().
# #
# # 👉 How will you use polymorphism to call draw() without checking the object type?

# dact type
# class Cricle:
#     def draw(self):
#         print("the cricle the draw the cricle")
#
# class Square():
#     def draw(self):
#         print("the Drawing the Square the draw the methods")
#
# class Triangle():
#       def draw(self):
#
#           print("the drawing the triangle the draws ")
# def shape(y):
#     y.draw()
# l=[Cricle(),Square(),Triangle()]
# for i in l:
#     shape(i)

# E-commerce Payment System
#
# An online shopping site supports multiple payment methods: CreditCardPayment, PayPalPayment, and UPIPayment.
#
# Each class has a method pay(amount).
#
#  How will polymorphism help the checkout system to call pay() method dynamically?
#
# class CreditCardPayment:
#     def pay(self ,Amount):
#         print(f"the shopping  as pyment{Amount}the will system ")
# class PayPalPayment:
#     def pay(self,Amount):
#         print(f"the shopping as PayPalpayment{Amount} ")
# class UPIPayment:
#     def pay(self,Amount):
#         print(f"the shopping as UPIpyment{Amount}system")
# def Shopping(x,Amount):
#     x.pay(Amount)
# Shopping(CreditCardPayment(), 1000)
# Shopping(PayPalPayment(),5000)
# Shopping(UPIPayment(),1000)
#

# Animal Sound Simulation
#
# You are creating a zoo simulation. Classes Dog, Cat, and Cow each implement a make_sound() method.
#
# 👉 How can polymorphism help you iterate over a list of animals and make them all produce their sounds?
#
# class Dog:
#     def make_sound(self):
#         print("the  dog make_sound bow bow")
# class Cat:
#     def  make_sound(self):
#         print("the  cat make_sound mau mauu..")
# class Cow:
#     def  make_sound(self):
#         print("the  Cow make_sound mau Bark..")
# def Animal(x):
#     x.make_sound()
# l=[Dog(),Cat(),Cow()]
# for i in l:
#     Animal(i)
#


# Employee Salary System
#
# A company has employees: FullTimeEmployee, PartTimeEmployee, Intern.
#
# Each class has a method calculate_salary().
#
# 👉 How would you use polymorphism to calculate salary for different employee types in a single loop?
class FullTimeEmployee:
    def calculate_salary(self, amount):
        print(f"The Full Time Employee Salary: {amount}")

class PartTimeEmployee:
    def calculate_salary(self, amount):
        print(f"The Part Time Employee Salary: {amount}")

class Intern:
    def calculate_salary(self, amount):
        print(f"The Intern Salary: {amount}")

def methods(x, amount):
    x.calculate_salary(amount)

#
l = [FullTimeEmployee(), PartTimeEmployee(), Intern()]

for i in l:
    methods(i, 5000)


# File Reader Utility
#
# You have classes for reading different file formats: TextFileReader, CSVFileReader, JSONFileReader.
#
# Each has a method read_file(filename).
#
# How can polymorphism allow a program to handle different file types seamlessly?
class TextFileReader:
    def read_file(self,filename):
        print(f"the are file is {filename} ")
class CSVfileReader(TextFileReader):
    def read_file(self,filename):
        super().read_file("jagtap.text")
        print(f"the are file name is {filename}")
class JSONFileReader(CSVfileReader):
    def read_file(self,filename):
        super().read_file("filereader.CSV")

        print(f"the are file name is {filename} ")
r=JSONFileReader()
r.read_file("Javascript.json")



# Transport Ticket Booking
# #
# A travel booking system has different transport modes: Bus, Train, Flight.
#
# Each implements a method book_ticket().
#
# 👉 How would you use polymorphism to let the user choose transport without writing multiple if-else conditions?
#
#
# class Bus:
#     def book_ticket(self):
#         print("the Bus ticket book successfully")
# class Train:
#     def booK_ticket(self):
#         print("the Train ticket book Successfully")
# class Fight:
#     def book_ticket(self):
#         print("the flight book successfully")
# def Transport(x):
#     x.book_ticket()
# if __name__=="__main__":
#     choice =input("Enter transport mode (bus/train/fight)--> ")
#     x_mode={
#         'bus':Bus(),
#         'train':Train(),
#         'fight':Fight()
#     }
#     x=x_mode.get(choice)
#     if x:
#         Transport(x)
# else:
#   print("Invalid choice!")



# Calculator with Multiple Operations
#
# You design a calculator with classes Addition, Subtraction, Multiplication, Division.
#
# Each has a method operate(a, b).
#
# 👉 How will polymorphism let you execute different operations dynamically using the same method name?
#
# class Add:
#     def operate(self,a,b):
#         print(a+b)
#
# class Subtraction(Add):
#     def operate(self,a,b):
#         super().operate(22,11)
#         print(a-b)
# class Multiplication(Subtraction):
#
#     def operate(self,a,b):
#         super().operate(34, 11)
#         print(a*b)
# M=Multiplication()
# M.operate(20,11)

# Online Education Platform
#
# In an LMS system, you have content types: VideoLecture, Article, Quiz.
#
# Each has a method display_content().
#
# 👉 How can polymorphism ensure that calling display_content() shows the right type of content?

class VideoLecture:
    def dispay_content(self):
        print("the ")

# Gaming Characters
#
# In a game, different characters exist: Warrior, Archer, Mage.
#
# Each class has a method attack().
#
# 👉 How would polymorphism allow you to call attack() without knowing which character you are controlling?
#
#
#
#
#
# Bank Loan Processing
#
# A bank has loan types: HomeLoan, CarLoan, EducationLoan.
#
# Each has a method calculate_interest().
#
# 👉 How will polymorphism help in processing loans without writing separate logic for each loan type?
#
#
#
#
# Abstraction  Qestions
#
#
#
#
#
# ATM Machine
#
# You are designing an ATM system.
#
#
#
#
#
# Customers should only see options like withdraw(), deposit(), check_balance().
#
#
#
#
#
# Internal details like PIN verification, connecting to the bank server, and updating the database should be hidden.
#
# 👉 How can abstraction help you design this system?
#
#
#
#
#
# Car Driving System
#
# When driving a car, a driver only interacts with steering, brakes, accelerator, and gear.
#
# Internal details like fuel injection, engine ignition, or ABS braking system are hidden.
#
# 👉 How would you implement this in Python using abstract classes?
#
#
#
#
#
# Online Payment Gateway
#
# A user pays through CreditCard, NetBanking, or UPI.
#
# The system should provide a common method make_payment(), while hiding the actual processing details.
#
# 👉 How can abstraction be applied here to simplify the payment process for the user?
#
#
#
#
#
# University Management System
#
# A university has different people: Student, Professor, and AdminStaff.
#
# All of them should implement a method get_role(), but the way it works is different for each.
#
# 👉 How can abstraction enforce a common structure while hiding implementation details?
#
#
#
#
#
# E-commerce Order Tracking
#
# Customers should only see the order status: Pending, Shipped, Delivered.
#
# They should not know the internal steps like warehouse updates, courier partner API calls, or inventory reduction.
#
# 👉 How can abstraction be used to design a clean interface for order tracking?
#
#
#
# Encapsulation Questions
#
#
#
#
#
# Bank Account Security
#
# A BankAccount class should store balance privately.
#
#
#
#
#
# Users can deposit() and withdraw() through methods.
#
#
#
#
#
# Direct access to balance should not be allowed.
#
# 👉 How will you use encapsulation to protect sensitive data like balance?
#
#
#
#
#
# Student Report System
#
# A Student class has private attributes like __marks.
#
#
#
#
#
# Teachers can update marks only using a method set_marks().
#
#
#
#
#
# Students can view their grade using get_grade(), but cannot directly modify marks.
#
# 👉 How can encapsulation ensure controlled access to marks?
#
#
#
#
#
# Online Shopping Cart
#
# In a ShoppingCart class, items and prices should be stored privately.
#
#
#
#
#
# Users should only add items via add_item() and view total via get_total().
#
#
#
#
#
# They should not directly manipulate item prices.
#
# 👉 How does encapsulation ensure data integrity in the cart?
#
#
#
#
#
# Employee Salary Management
#
# An Employee class should have private attributes like __salary.
#
#
#
#
#
# Salary should only be modified by set_salary() with validation (e.g., no negative salary).
#
#
#
#
#
# It should be accessed using get_salary().
#
# 👉 How can encapsulation help in preventing wrong salary updates?
#
#
#
#
#
# Game Character Health
#
# A Player class has a private variable __health.
#
#
#
#
#
# Health can only be reduced or increased using methods like take_damage() or heal().
#
#
#
#
#
# Direct access to __health should be restricted.
#
# 👉 How can encapsulation protect player health values from accidental modification?
#
#
#
#
# By Using all four Pillers
#
#
#
# 🔹 Question 1: Library Management System
#
# Design a Library system with the following requirements:
#
#
#
#
#
# Encapsulation → Keep book details like __title, __author, __copies private, and provide getters/setters.
#
#
#
#
#
# Abstraction → Define an abstract class LibraryItem with abstract methods like display_info() and borrow().
#
#
#
#
#
# Inheritance → Create subclasses Book, Magazine, and DVD that inherit from LibraryItem.
#
#
#
#
#
# Polymorphism → Implement display_info() and borrow() differently in each subclass.
#
#
# 👉 How would you design the classes so the system can handle multiple item types with the same interface?
#
#
# 🔹 Question 2: Vehicle Rental System
#
# Design a VehicleRental system with these features:
#
#
#
#
#
# Encapsulation → Keep attributes like __vehicle_id, __rent_price private with controlled access.
#
#
#
#
#
# Abstraction → Create an abstract class Vehicle with abstract methods calculate_rent(days) and vehicle_info().
#
#
#
#
#
# Inheritance → Implement Car, Bike, and Truck as subclasses of Vehicle.

#
#
#
#
#
# Polymorphism → Each subclass should calculate rent differently (Car = daily rent, Bike = hourly rent, Truck = weight-based rent).
#
#
# 👉 How will OOP pillars help you design a flexible system where new vehicle types can be added easily?
#
#
#
# Sep 22 - 4:21 pm
