# Decorator / Meta_programing :
# syntax:
# def outer(main_function):
#     def inner(*args,**kwargs):
#         #statement
#
#         main_function(*args,**kwargs)
#     return inner
#
# @outer                              # connection
# def main_function(parameter):
#     #statement
#
# main_function(argument)
import time


# def outer(func):
#     def inner(*args,**kwargs):
#         print('welcome ')
#         func(*args,**kwargs)
#     return inner
#
# @outer                                 # connection
#
# def Greet():
#     print('hello python')
# Greet()

# def outer(Greet):
#     def inner(*args,**kwargs):
#         print('welcome ')
#         Greet(*args,**kwargs)
#     return inner
#
# @outer
#
# def Greet():
#     print('hello python')
# Greet()

# def outer(func):
#     def inner(x,y):
#         print('i am doing addition operation')
#         func(x,y)
#     return inner
# @outer
# def Add(x,y):
#     print(x+y)
# Add(10,20)

# def outer(func):                         # 1
#     def inner(a,b):                      # 3
#         print('multiplication ')         # 6
#         func(a,b)                        # 7
#     return inner                         # 4
# @outer                                   # 2
# def mul(a,b):
#     print(a*b)                           # 8
# mul(12,5)                                # 5

#
#
#
#
# # Adding functinality without changing the main function is called Decorators
# # A Decorators is a function which takes another function as an argument ,add some extra
# # functionality and return another function without altering the source code of the original function.
#
#
# #Decorators also called as Meta Programming
# # reason:--->A part of the program Tries to modify another part of the program at compile time
#
# #General structure of decorator
# def outer(fun):
#     def inner(a,b):
#         if a<b:
#             a,a=b,a
#         return fun (a,b)
#     return inner
# @outer
# def div(a,b):
#     print(a/b)
# div(2,4)
#
#
# def addition(fun):
#     def inner(*args):
#         print("in performing addition")
#         fun(*args)
#         print("addition is done")
#     return inner
# @addition
# def add (*args):
#     c=sum(args)
#     print(c)
# add(1,2,3,4,5,6,7)



#
#
# # step-3
# def outer(fun):
#     def inner(*args,**kwargs):
#         res = fun(*args,**kwargs)
#         return (abs(res))
#     return inner
# @outer
# def sub(a,b):
#     return a-b
# print(sub(-20,2))

# 4.wap to create A decorator function that measures
# the execution time of the function and print it

#
# from time import sleep
# def outer(fun):
#     def inner():
#        start=time.time()
#        fun()
#        end=time.time()
#
#        execution_time=end-start
#        print(f"{fun.__name__}"
#              f"{execution_time} seconds")
#        return inner
# @outer
# def display():
#     sleep(4)
#     for i in range(1,11):
#         print([i],end="")
# display()
#
#
#
# Decorators Examples
#
#
# 1.write a decorator function that prints "HELLO EVERYONE" message before execute any function
# def Outer(fun):
#     def inner():
#         fun()
#         print("the Hello Everyone ")
#
#     return inner
# @Outer
# def Main_fun():
#     for i in range(1,6,1):
#         for j in range(i):
#             print("*", end=" ")
#         print()
#
# Main_fun()







# 2.write a decorator function to print main function name before executing any decorator function
# from time import time
# def Outer (fun):
#     def inner():
#         start=time.time()
#         print(" the are adding functioality with out changing main function is colled as decorators", fun().__name__)
#
# def Function():
#     print("the write a decorator function to print main function name before exceuting any decorator function")
# Function()
#
# #
# 3.write a decorator which inputs 5 seconds of delay before executing any decorator function
# from time import sleep
# def Outer(fun):
#     def inner():
#         sleep(5)
#         a=eval(input("the Enter number---> "))
#         sleep(5)
#         b=eval(input("the Enter the number--->"))
#
#         fun(c=a+b)
#     return inner
# @Outer
#
# def Function(c):
#     print("the add input 5 second")
#     sleep(5)
#     print(c)
# Function()
# 4.write a decorator function calculate the execution time of any function
# from time import time
# import time   #  import time module
#
# def Outer(fun):
#     def inner():
#         start = time.time()   # call time() function properly
#         for i in range(6, -1, -1):   # loop from 6 down to 0
#             for j in range(i):
#                 print("*", end=" ")
#             print()
#         end = time.time()
#         fun(end)
#     return inner
#
# @Outer
# def Function(Nato):
#     print("Execution Time:", Nato)
#     print("The decorator function calculated the execution time.")
#
# Function()

# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the original function
# def Outer(fun):   # function name matches the decorator
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return fun(a, b)
#     return inner
#
# @Outer
# def division(x, y):
#     return x / y
#
# # Test
# print(division(2, 10))  # swapped → 10 / 2 = 5.0
# print(division(2, 2))   # no swap → 2 / 2 = 1.0

#
# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"
# from time import sleep
# def add(fun):
#     def inner():
#         print("the Iam doing addition operation")
#         a=eval(input('the Enter  Value----> '))
#         b=eval(input("the Enter Value---> "))
#         fun(a+b)
#     return inner
# @add
#
# def display(fun):
#     sleep(5)
#     print(fun)
#     print("addition opetration is dane")
#
# display()
# o/p--->i am doing addition operation"
#        value
#      "addition operation is done
#
#
#
# 7.create a decorator to return only positive out from any subtraction
#
#
# 8.create a decorator which counts the number of function calls
#
#
#
# 9.wap to sum of the positional arguments and get the length of the keywords arguments
# def Outer(fun):
#     def inner(*args,**kwargs):
#         print(f"the total length of Kwargs{len(kwargs)}")
#         print(f" the total sum is args{sum(args)}")
#         fun(*args,**kwargs)
#     return inner
# @Outer
# def spam(*args,**kwargs):
#     print(sum(args))
# spam(12,3,4,5,6,7,c=3,d=2,g=6)
#
# 10.write a decorator function to print the type of datatype before performing the action
# def Outer (fun):
#     def inner(*args):
#         for i in args:
#             print(type(i))
#         fun(*args)
#     return inner
# @Outer
# def demo(*args):
#     print(args)
# demo(1,2,34,5,[12,32,11,11],{1,23,4,13,4})
# 11.write a decorator operation on the given number and the condition is A>B then perform multiplication in decorator function else
#  cube it in decorator
# def Outer(fun):
#     def inner(a,b):
#         if a>b:
#             print(f"the Value is  {a*b}")
#         else:
#             print(f"the Value is cub is {a**b}")
#
#     return inner
# @Outer
# def Opration(a,b):
#     print(a+b)
# Opration(10,20)



# 12.create a decorators to which prints name of called main function and counts the function calls
#
# def outer(fun):
#     count = 0  # counter inside closure
#
#     def inner(*args, **kwargs):
#         nonlocal count  # so inner can modify count
#         count += 1
#         print(f"Function called: {fun.__name__}")
#         print(f"Call count: {count}")
#         return fun(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def Count(*args):
#     print("Function executed with args:", args)
#
#
# # Test
# Count(1, 2, 4, 566)
# Count(10, 20)
# Count()
#

# 13.create a decorators to which prints names of called functions and checks the number is even or odd
# def Outer(fun):
#     def inner(*args):
#         for i in args:
#             if i % 2 == 0:
#                 print(fun.__name__)
#                 print(f"{i} is an even number")
#             else:
#                 print(f"{i} is an odd number")
#         return fun(*args)
#     return inner
#
# @Outer
# def checks(*args):
#     print("Original function received:", args)
#
# # Test
# checks(1, 234, 54, 34)


#
# 14.create a decorator which delays its execution as per user input
# import time
# def decorator():
#     print("the create a decorator which delays")

# # # 15.write a multilevel decorator to log some message
# import time
#
# def Outer(fun):
#     def inner(*args, **kwargs):
#         time.sleep(5)
#         for i in range(1, 11):
#             print(i)   # print the number
#             fun(*args, **kwargs)
#     return inner  # <-- return must be here
#
# def Outer1(fun):
#     def inner(*args, **kwargs):
#         time.sleep(5)
#         for i in range(1, 11):
#             if i % 2 == 0:
#                 print(i)   # print only even numbers
#             fun(*args, **kwargs)
#     return inner  # <-- return must be here
#
# @Outer
# @Outer1
# def multiple():
#     print("Inside multiple function")
#
# # Call the function
# multiple()
#


# 16.write a multilevel decorators to accept username and register number of employee
# import time
# def name(fun):
#     def inner(*args):
#         a=(input(f"Enter the name:--"))
#         fun(*args)
#     return inner
# def register(fun):
#     def inner(*args):
#         time.sleep(5)
#         a=eval(input(f"Enter the register:--"))
#         fun(*args)
#     return inner
# def number(fun):
#     def inner(*args):
#         time.sleep(5)
#         a=int(input(f"Enter the number:--"))
#         fun(*args)
#     return inner
# @name
# @number
# @register
# def seep():
#     time.sleep(5)
#     print("operations in dones")
# seep()
# 17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
#  DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER
# form time import time()
# def Outer(fun):
#     def inner(a):
#         sleep(5)
#
#     return  inner
# @Outer
# def Data1(name):
#     print(f"this is a name{name}")
# @Outer
# def Data2(email):
#         print(f"this is a name{email}")
# @Outer
# def Data3(number):
#     print(f"this is a name{number}")
# #
# 18 using 3 decorators show me one example

# import time
# def OUter(fun):
#     def inner(a,b):
#         time.sleep(3)
#         fun(a,b)
#     return  inner
# @OUter
# def add(a,b):
#     print("the two values addition is this formation the are is most importin")
#     print(a+b)
# add(12,221)
#
# @OUter
# def sub(a,b):
#     print("this operation is subraction")
#     print(a-b)
# sub(12,11)



# def outer(spam):
#     def inner(*args,**kwargs):
#         print("Good morning")
#         spam(*args,**kwargs)
#     return inner
# @outer
# def spam():
#     print("spam methods")
# @outer
# def dispaly():
#     print("the are display methods")
# spam()
# dispaly()
# def Outer1(fun):
#     def inner(*args,**kwargs):
#         print("*")
#         fun(*args,**kwargs)
#     return inner
# def Outer(fun):
#     def inner(*args,**kwargs):
#         print("@@@@@@@@@@")
#         fun(*args,**kwargs)
#     return inner
# @Outer1
# @Outer
# def  Demo():
#     print("Decorator..........methods")
#
#
# @Outer1
# @Outer
# def wrapper():
#     print("wrapper class methods...")
# Demo()
# wrapper()

#
# import time
# def outer(fun):
#     def inner(x,y):
#         time.sleep(5)
#         print("waiting for the result def inner methods")
#         fun(x,y)
#     return inner
# @outer
# def sub(x,y):
#     time.sleep(5)
#     print(x-y)
# sub(10,5)




#
# def outer(fun):  #####-------------------memory address will be created
#     def inner(*args,**kwargs):
#         print("this is decorator function in python")
#         fun(*args,**kwargs)         fun== div
#     return inner
# @outer                                #------div=outer (div)
# def main_f(a,b):
#     print(f"addtion of two operators{a+b}")
# main_f(10,20)
#



# # Delay decorators
# from time import sleep
# def outer (fun):
#     def inner(*args,**Kwargs):
#         print("the time module using Delay decorators ")
#         start=time.time()
#         sleep(4)
#         fun(*args,**Kwargs)
#         end=time.time()
#         print(end-start)
#     return inner
# @outer
# def add(a,b):
#     print(f"addition of two numbers {a+b}")
#
# add(12,34)
#
# @outer
# def sub(a,b):
#     print(f"subtraction of two numbers {a-b}")
# sub(10,5)
#
#
# from time import sleep
# print("Employee Details")
# def outer(fun):
#     def inner(*args,**Kwags):
#         print(f"my function name is {fun.__name__} ")
#
#         sleep(3)
#         fun(*args,**Kwags)
#     return inner
# @outer
# def display_name():
#     res=input("enter the employee name--> ")
#     print(f"The employee name is--{res}")
# @outer
# def display_email():
#     res1=input("the Enter your email---> ")
#     print(f"The employee name is--{res1}")
# @outer
# def display_number():
#     res2=input("the Enter your number---> ")
#     print(f"the employee number is--{res2}")
# display_name()
# display_email()
# display_number()

# from time import sleep
# def outer_most(x):
#     def outer(fun):
#         def inner(*args,**kwargs):
#             start=time.time()
#             sleep(3)
#             print(f"this is function name---> {fun.__name__}")
#             print(x)
#             end=time.time()
#             fun(*args,**kwargs)
#             print(end-start)
#         return inner
#     return outer
# @outer_most("good morning")
# def spam():
#     print("this methods is spam")
# @outer_most("good afternoon")
# def check():
#     print("the are check methods")
# @outer_most("good evening")
# def mayur():
#     print("one methods")
# spam()
# check()
# mayur()
#

#
#
# def Bank_Acc(message):
#     def outer(func):
#         def inner(*args,**kwargs):
#             # bal=int(input("Enter the amount--> "))
#             print(f'[BANK LOG] {message}')
#             func(*args,**kwargs)
#             print('-'*30)
#         return inner
#     return outer
#
# @Bank_Acc('opening a new account')
# def open_account(name,balance):
#     print(f'Account open for name {'shane watson'}'
#           f' with balance is rs {100000}')
#     return balance
# @Bank_Acc('Depositing Money')
# def deposit(name,amount,balance):
#     new_bal=amount+balance
#     print(f'{amount} deposited successfully'
#           f' in account name is {name}\n'
#           f'update balances{new_bal}')
#     return new_bal
# @Bank_Acc('withdrawl money')
# def withdraw(name , amount,bal):
#     print(f'the {amount-bal} withdraw successfully in account name in {name}')
#
# open_account('shane watson',100000)
# deposit('shane watson',25000,200)
# withdraw('shane watson',30000,200)

#
# from time import sleep
# def outer_most(x):
#     def outer(fun):
#         def inner(*args,**kwargs):
#             sleep(3)
#             print(x)
#             print(f"this is function name---->{fun.__name__}")
#             fun(*args,**kwargs)
#         return inner
#     return outer
# @outer_most ("this a first function")
# def main():
#     print("this is a main function")
# @outer_most ("this is a second function")
# def spam():
#     print("this function is spam messages")
# main()
# spam()
#
