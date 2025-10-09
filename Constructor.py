# # # step--->normal way of constructor
# # class Evening:
# #     def __init__(self):
# #         print("Evening Class")
# #     def demo(self):
# #         print("demo methods")
# #     def __init__(self):
# #         print("construtor _class")
# # e=Evening()
# # e.demo()
# # e.__init__()
#
#   ### without passing parameter
# class bank:
#     def __init__(self):
#         Bank_name="ICIC"
#         Account_holder_name="Mayur"
#         Account_NUmber=12345432
#         account_Balance=43234
#         Ifsc_code="ICLp123432"
#         LOcation="pune"
#         print(f"My bank name is{Bank_name} and Account Number is are{Account_NUmber}"
#               f"and Account Holder name is a{Account_holder_name} this prasan bank balance is"
#               f"{account_Balance}and Ifce code is a{Ifsc_code}and location of bank is {LOcation}")
# e=bank()
#
#
# ## with passing parameter
# class College:
#     def __init__(self,Class_name,dept_Name,techar_Name,Student_name,Account_section,):
#         print(f"the student name is{Student_name} this isa class name are{Class_name}"
#               f"and this is depatment name is a {dept_Name} and teachar {techar_Name} Acconut section is are {Account_section}")
# c
# =College("BBA","Commercs","Mayur","Avinash","mani")
from module import factorail


#using instance variable
class flipkart:
    def __init__(self):
        self.product_name="Mobile"
        self.price=1231
        self.location="Pune"
    def Product_information(self):
        print(f"My product_name is{self.product_name}and total \n price is{self.price}"
              f"My current location is {self.location}")
obj=flipkart()
obj.Product_information()



# def Uppercase_lowerCase():
#     i=ord("A")
#     j=ord("a")
#     while i < ord("Z") and j < ord("z"):
#         print(f"{chr(i)},{chr(j)}",end="")
#         i+=1
#         j+=1
#
# Uppercase_lowerCase()
#
#
# def fibonacci(x):
#     a ,b=0,1
#     i=0
#     while i <= x:
#         print(a ,end=" ")
#         a ,b =b ,a+b
#         i+=1
#
# fibonacci(12)


#
# def Factorial(x):
#      if x==0:
#          print("the not count number as factoral ")
#      else:
#          return x*factorail(x-1)
# print(factorail(5))
#
# def prime(x):
#     count=0
#     i=1
#     while i <= x:
#         if x%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print(f"this is a prime number {x}")
#     else:
#
#         print(f"this is a  not prime number {x}")
#
# for i in range(5):
#     prime(x=int(input("Enter the number--> ")))






a=123

def reverse(a):
    digit=0

    for i in range(a):
        digit=a%10
        rev=rev*digit+10
        digit//=10
    return digit
print(reverse(a))


