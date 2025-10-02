# # function python
#user defined function
# pre-defined
# these are the function which are already presen in S/W and will utilize the as pre_defind function
#we can't modify the pre-defined function
# print(),input(),len(),type(),isinstance(),int(),
# list(),
# user defined function
# these are the function which are defined /developed by the user based on customer requirement specification is called auser dwfined function
#     sefto perform addition an
# d subraction if "a"
# # is greater than b return sum else return difference
# def Operation(a,b):
#     if a>b:
#         return a+b
#     else:
#         return a-b
# print(Operation(11,5))
# print(Operation(12,21))

#  # 2.waf to check string is palindrome ro not (take user input)
# def palindroime(a):
#     if a==a[::-1]:
#         print(" this is number Palindrome")
#
#     else:
#         print(" this is not number Palindrome")
#
# palindroime(a=input( 'Enter the numbe'))

# # 3.wap to return length of variable keyword arguments
# def check(**kwages):
#     return len(kwages)
# x=check(a=90,b=100,c=23,d=32,f=67)
# print(x)
#  OR
# def check(**kwargs):
#     print(len(kwargs))
# n=check(name='Jagtap',first="Nimbraj",age=21)
# print(n)

# # 4.wap tp return length of the varible positional argument
# def Great(*args):
#     return (args)
# w=Great(1,2,3,4,5)
# print(w)
# print()

# def greate1(*args):
#     print(len(args))
# greate1(1,2,3,4,5)

#
# # wap  squaring of the element inthe give list
# l=[1,2,3,4,5,6,7,8,9]
# def Square(*x):
#   k=[]
#   for i in x:
#       k.append(i*2)
#   print(k)
# Square(*l)
     # # wap to fetch last digit numbers
# def Last_number(a):
#     return a%10
# d=Last_number(123)
# print(d)


# wap to read 3 number from the user, first two numbers
# should be added and the result of addition should
# be subtracted by thrid number
# def number(a,b,c):
#        d=a+b
#        k=d-c
#        return k
# x=number(11,32,23)
# print(x)


## wap to find square ,cube ,square, root
# and cube root of a number
# def Root(a):
#     return a**2,a**3,a**0.5,a**0.333
# n= Root(5)
# print(n)

#
# import math
#
# from loops import alphabets
#
#
# def New_way(y):
#     return  math.sqrt(y),math.cbrt(y),math.factorial(y)
# Q=New_way(5)
# print(Q)

#
# # wap to check the give character  is alphabets or digit or special character
# def checking(s):
#     if s.isalpha():
#         print(s)
#     elif s.isdigit():
#         print(s)
#     else:
#         print(s)
#
# checking('abc')
# checking('123')
# checking('#$$%')
#
#
# def Checking(s):
#     if s.isalpha():
#         print("its alphabet")
#     elif s.isdigit():
#         print("its a number")
#     else:
#         print("special character")
# x=Checking("abc")
#
#
# def op(a,b):
#     if a>b:
#         return a+b
#     else :
#         return a-b
# x=op(3,5)
# print(x)


# #### write a function to print the below
# # ## output
# # ## function("TRACXN",O)
# # PRINT TAX
# def function(w,i):
#     return w[i::2]
# R=function("TRACXN",0)
# print(R)
#
#
#
# # print RCN
# def Prin(w,i):
#      return w[i::2]
# N=Prin("TRAXCN",1)
# print(N)

# #  14  A function take varible number of position arguments  as input .
# # how to check if checking if the argument are more than 5
# def argument(*args):
#     if len(args)>=5:
#         print("this argument position more than 5")
#     else:
#         print("this argument position less than 5")
# argument(1,2,3,4,5)
# argument(12,34,21,11)


## wap to return a dictionary with character and ascii value pare
# s="It yours day"
# def acii(kwargs):
#     d={}
#     for i in kwargs:
#         d[i]=ord(i)
#        or
#        d.update({i:ord(i)})
#     print(d)
# acii("It yours day")
#


#  #### wap  to iterable if you are passing string or
#  # list or tuple else print() type of the data
# def iterable(*data):
#      for item in data:
#          if isinstance(data,(list,tuple,dict,set,str)):
#              print(data[::-1])
#          else:
#              print(type(data))
# iterable(1,2,34,34,12,33)
# iterable(23)
# iterable(23)
# iterable("python si most importain language")
# iterable("python si most importain language")
# iterable([23,12,3,45,6,7,4])
# iterable({23:12})
#


# # Function to check if a number is even or odd
# def check(num):
#      if num%2==0:
#         print("the user give number is even ")
#      else:
#          print("the user give number is odd")
# check(12)
# check(4)
# check(5)

##
# # Function to find factorial
#
#  # check if a number is prime
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(11))
# print(is_prime(13))
# print(is_prime(14))
# print(is_prime(12))
# print(is_prime(15))


#  # factorial using function
# def factorial(n):
#     if n<2:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=factorial(4)
# print(n)
#


# def fibonacci(n):
#     a, b = 0, 1   # first two Fibonacci numbers
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
# fibonacci(10)

#
# def fibonacci(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end=' ')
#         a,b=b,a+b
# fibonacci(int(input( "the enter number")))

# ## check palindrome string
# def is_palindrome(num):
#     if num == num[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome("123"))
# print(is_palindrome("madam"))
# print(is_palindrome("dad"))
#
#

     # check Armstrong Number
#
# def Arms(n):
#     power=len(str(n))
#     total=sum(int(d)**power for d in str(n))
#     return total==n
# print(Arms(5))
# print(Arms(10))
2
# # find Gcd (greatest common Divisor)
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# def lcm(a, b):
#     return a * b // gcd(a, b)
# print(lcm(2, 3))
# print(gcd(2, 3))

