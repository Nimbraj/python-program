# # Step 1
# class Evening:
#     @classmethod
#     def Display(cls):
#         print("Evening class")
# e=Evening()
# e.Display()  # To Access Data through object
# Evening.Display()  ## To Access Data through Class_Name
#
# ## Step2----> in the place of cls another character
# class Evening:
#     @classmethod
#     def Display(X):
#         print("Evening Class")
# e=Evening()  ## To Access Data Through object
# e.Display() ## To Access Data through Class _name
#
#
#
# ## Step 3
# class Evening:
#     @classmethod
#     def Display(X):
#         print(X)
# e=Evening()
# print(e)
# e.Display()
#
# class Evening:
#     @classmethod
#     def demo(cls,total_count):
#         print(f"Total count of the class{total_count}")
# e=Evening()
# e.demo(30)
# Evening.demo(40)

# class Student:
#     @classmethod
#     def subject1_details(cls):
#         name="PYTHON"
#         Hour="45hour"
#         days=25
#         print(f"subject name is a{name} and total hours will be {Hour}"
#               f"and days is a{days}")
#     @classmethod
#     def Data(cls):
#             mock="1"
#             mock2="*"
#             print(f"first subject Rating is {mock} and second subject rating is{mock2}")
# z=Student()
#
# z.subject1_details()
# z.Data()
# print()
# St8udent.subject1_details()
# Student.Data()
#
#
#
# class Exam:
#     Date="30/08/2025"
#     @classmethod
#     def Day1_exam(cls):
#         print(f"my exam date is {Exam.Date}")
#
#     @classmethod
#     def Day2_exam(cls):
#         print(f"my exam date is {Exam.Date}")
#     @classmethod
#     def Day3_exam(cls):
#         print(f"my exam date is {Exam.Date}")
# e=Exam()
# e.Date="31-08-2025"
# e.Day1_exam()
# e.Day3_exam()
# e.Day3_exam()
