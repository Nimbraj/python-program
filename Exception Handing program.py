# try block
from Inheritance import x

# except block

# else block

# finally block --->  keywords it will be not matter any error
#

#
# d=[1,2,3,4,5]
# try:
#    print(d[13])
# except IndexError:
#     print("index error handled")
# else:
#     print("NO error")
# finally:
#     print("execution is completed")
#

########## nested try exception block############

# Syntax:----->
# try:
#       NOerror

# except:
#     statement/handline line line


###################
# a=10
# b=5
# try:
#     print(a/b)
#     try:
#         # print(a/c)
#         print(a*b)
#     except NameError:
#         print("Name error handled")
#     else:
#         print("code is executed")
# except:
#     print("NO error")
# finally:
#     print("the handling all block")

### USER DEFINED ERROR##################


#   ###  raise   ---->keywords
# #   # syntax
#        class  user_defined_error (Exception/BaseException):
#                  pass/....
#





#class metroError (Exception):
#     pass
#     def demo(self):
#         if x==0:
#              print("+tive number")
#         else:
#             raise metroError
# e=metroError
# e.demo(-10)



#
# class invlaidpasswords(BaseException):
#     ...
#     def length(x):
#         if x==10:
#             print("vaild error")
#         else:
#             raise invlaidpasswords
# e= invlaidpasswords
#
# e.length(12)

# try:
#     file=open("python.tex","r")
#     print(file.read())
# except:
#     print("file not found error handled")
#

#
# try:
#     age=int(input("enter the number--->"))
# except ValueError:
#       print("value error handling")



















