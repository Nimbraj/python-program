# ##########   Generator  ########
# ##wap to  return a iterator having tuple of
# # word and its len pari and typecast into dictionary
# z=["instagram","facebook","whatsapp","meta","oracle"]
# def typecast(z):
#     d ={}
#     for i in z:
#         d[i] = len(i)
#         yield d
# x=typecast(z)
# for i in x:
#     print(i)


# # wap to generate only numeric values in given list
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def numbers(a):
#     for i in a:
#         if type(i) in (int ,float,complex,bool):
#             yield i
# x=numbers(l)
# print(list(x))


# wap to generate a list if it is individual data type
# # reverse it else return its type of the data
# l=["flipkart",'Amazon',78,[2,3,4,],78,9.87,(5,3),48.36]
# def reverse(l):
#     for i in l:
#         if type(i)  in (int,float,complex,bool):
#
#             yield str(i)[::-1]
#         else:
#             yield type(i)
#
# x=reverse(l)
# print(list(x))
#
# # wap to create a list of numbers if nu
# # mber are even square it else cube it
# l=[2,3,4,5,6,7]
# def square(l):
#     for i in l:
#         if i%2==0:
#             yield(i**2)
#         else:
#             yield(i**3)
# x=square(l)
# print(list(x))

# wap to generate the first letter
# # of the word as key and words starting with letter as value
# s="python is a programming language and programming is part of life"
# def key(s):
#     d={}
#     for i in s.split():
#         if i[0] not in d:
#             d[i[0]]=[i]
#     else:
#         d[i[0]]+=[i]
#     yield(d)
# w=key("python is a programing language and programming is part of life")
# print(list(w))  
#
#

# Functions
#
# Definition: A function is a block of reusable code that performs a specific task.
#
# Why use functions?
# Code reusability
# Modularity (breaking big problem into smaller)
# Readability
# Easy maintenance
#
#code reusable code that performs a specific task...
# 2. Types of Functions
#
# Built-in functions → len(), max(), min(), print(), type()...
# User-defined functions → Functions created by the programmer.
# Lambda (Anonymous) functions → Single line functions using lambda.
#
# 3.Function Parameters
# Types:
# Positional arguments
#
# def greet(name, age):
#     print(f"Hello {name}, age {age}")
# greet("Alice", 25)
#
#
# Keyword arguments
# greet(age=30, name="Bob")
#
#
# Default arguments
# def greet(name, age=18):
#     print(f"Hello {name}, age {age}")
# greet("Charlie")  # age = 18`
#
#
# Variable length arguments
# *args → Non-keyword arguments (tuple)
# **kwargs → Keyword arguments (dict)
#
# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# demo(1, 2, 3, a=10, b=20)
#
# 🔹 4. Scope & Lifetime of Variables
#
# Local variable → Declared inside a function, accessible only there.
#
# Global variable → Declared outside function, accessible everywhere.
#
# global keyword → To modify global variable inside function.
#
# nonlocal keyword → To modify variable in nested function.
#
# 🔹 5. Return Statement
#
# return ends function execution and sends a value back.
# A function without return returns None.
# def add(a, b):
#     return a + b
#
#
# 6. Packing & Unpacking Arguments
# def demo(a, b, c):
#     print(a, b, c)
#
# nums = [1, 2, 3]
# demo(*nums)  # unpack list → 1 2 3
#
# params = {"a": 10, "b": 20, "c": 30}
# demo(**params)  # unpack dict
#
# """


##Positional only argument
# the used of ---->(/)
def mul(a,b,c,/):
    print(a*b*c)
mul(2,4,7)

# keywords only argument
# def sub(*,b,c):
#     a=b-c
#     return a
# print(sub(b=10,c=5))
#
# def add(b,c,/,*,f,d,):
#     a=b+c
#     g=f+d
#     return a,g
# print(add(20,30,f=50,d=30))

# variable positonal only argument()


def add (a,b):
    return a+b
print(add(10,20))
# Function to find factorial of a number
# n=int(input("the Enter number---> "))
# def factorial_numbers(n):
#     return  1 if n==0 else n*factorial_numbers(n-1)
# print(factorial_numbers(n))


# function odd even numbers check
# number=int(input("the Enter you number----> "))
# def Check(number):
#     if number%2==0:
#         print(f"this number is even --> {number}")
#     else:
#         print(f"this number is odd{number}")
# Check(number)

#wap function using fibonacci
# n=int(input("the enter number---> "))
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end= ' ')
#         a,b=b,a+b
# fibonacci(n)

# factorial number
# f=int(input("the Enter number--> "))
# def factorial(n):
#     return 1 if n==0 else n*factorial(n-1)
# print(factorial(f))




# # fibonacci program
# number=int(input("the Enter number--->"))
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(f"{a}",end=" ")
#         a,b=b,a+b
# fibonacci(number)
#
#
#


# function to find maximun of three numbers
# def maximum(a,b,c):
#     return max(a,b,c)
# print(maximum(10,32,56))
#
# n=int(input("The Enter number---> "))
# def reverse_number(n):
#     rev =0
#     while n >0:
#         digit = n % 10
#         rev =rev * 10 +digit
#         n//=10
#     return rev
# print(n)
# print("reverse ",reverse_number(n))

# n=int(input("the enter number-->"))
# def revrese(n):
#     m=str(n)
#     return m[::-1]
# print(n)
# print("reverse",revrese(n))


# function to check palindrome
# def is_palindrome(n):
#     if n==n[::-1]:
#         print(f"this  is a palindrome {n}")
#     else:
#         print(f"this  is a not palindrome {n}")
#
#
# print(is_palindrome("mam"))

/
# def Count_vowels(n):
#     for i in n:
#         if i in ("aeiouAEUIO"):
#             print(i)
# Count_vowels("Hello world")






# def is_prime(n):
#     if n<2: return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i ==0: return  False
#         return tr
