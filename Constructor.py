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
# c=College("BBA","Commercs","Mayur","Avinash","mani")

#using instance variable
class flipkart:
    def __init__(self):
        self.product_name="Mobile"
        self.price=1231
        self.location="Pune"
    def Product_information(self):
        print(f"My product_name is{self.product_name}and total price is{self.price}"
              f"My current location is {self.location}")

