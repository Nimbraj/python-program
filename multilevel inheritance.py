#
#
#
# class Data:
#     def Demo(self):
#         print("the methods is a instances methods")
#     def checK(self):
#         print("this methods a Check methods a Data Class")
# class test(Data):
#     def  Test(self):
#         super().Demo()
#         print("this methods  is used to are is multiple Test class")
#     def checK(self):
#         super().checK()
#         print("the one class Data tecke anothe class is colled as inheritance ")
# class Information(test):
#     def infirmation(self):
#         super().Test()
#         print("the child class tek propertic  in parent class tis called as single level inheritance ")
#     def checK(self):
#         super().checK()
#         print("The child class tek propertic in inter parent class iner class tek propertic s"
#               " parent class this called as multi level inheritance")
# i=Information()
# i.checK()
# i.infirmation()
#
#
# class Morning:
#     def Sql(self,Trainer_name):
#         print(f"sql class----->{Trainer_name}")
#     def Subject_mock(self,day,rating):
#         print(f"total "
#               f"sql mock taken day{day}and final rating is a {rating}")
# class Afternoon(Morning):
#        def Manual(self,Taniner_name):
#            super().Sql("vikash sir")
#
#            print(f"Manul class----->{Taniner_name}")
#        def Subject_mock(self,total_Student,Star_Student):
#            super().Subject_mock(34,"*")
# class Evening(Afternoon):
#     def Python(self,Tainer_name):
#         super().Manual("mayur sir")
#
#         print(f"python Class ---->{Tainer_name}")
#
#     def subject_mock(self,class_room,):
#         super().Subject_mock(35 ,"12")
#         print(f"the mork room is are {class_room}")
# E=Evening()
# E.Python("RAM")
# E.subject_mock("4")


# Parent Class 1
class Customer:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no

    def show_customer(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.acc_no}")


# Parent Class 2
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def show_bank(self):
        print(f"Bank Name: {self.bank_name}")


# Child Class (Multiple Inheritance)
class Account(Customer, Bank):
    def __init__(self, name, acc_no, bank_name, balance):
        Customer.__init__(self, name, acc_no)   # Initialize Customer
        Bank.__init__(self, bank_name)          # Initialize Bank
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")
        else:
            print("⚠ Insufficient Balance!")

    def show_account(self):
        print("\n--- Account Details ---")
        self.show_customer()
        self.show_bank()
        print(f"Balance: {self.balance}")


# Example Usage
acc1 = Account("Nimbaraj", 123456, "HDFC Bank", 5000)
acc1.show_account()

acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(5000)
