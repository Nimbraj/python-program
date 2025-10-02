# # Anonymous function is a function that is defined without a def key words
# # Anonymous function will be defined by using "lambda"
# # return keywords
# # we can't used for loop
# # we cna't used =,+=
# # Syntax
# # variable_name=lambda args1,args2:true statement expression
#
#
# # square=lambda i:i**2
# # print(square(5))
# # wap to check if the if the number is even or odd
# # number=lambda i:"this number is even  " if i%2==0  else "this number is odd"
# # print(number(14))
# # import math
#
# # h=[1,2,3,45,3]
# # l=[]
# # for i in h:
# #     l.append(i**2)
# # print(l)
#
# #
# # # a=lambda h:[i**2 for i in h]
# # # print(a([1,234,5,78,9]))
# # # x={23:78,100:34,'a':"b",'d':'b'}
# # #
# # # q1=lambda x:x.values()
# # # print
# # # (q1(x))
# #
# #
# # # n={23:78,100:34,'a':"b",'d':'b'}
# # # q1=lambda n: n.items()
# # # print(q1(n))
# #
# #
# # # wap to print both position and element
# # s=[100,500,345,789,900,231,111]
# # a=lambda s:[(i,j)for (i,j) in enumerate (s)]
# # print(a(s))
# # s="good luck"
# # # o/p (("good luck ,9"),{"good luck:9"})
# # a=lambda s:[(s,len(s),{(s):len(s)} )]
# # print(a(s))
#
#
#
# # x=lambda a:(lambda b:(a+b))
# # print(x(10)(20))
#
#
# # #
# # # Lambda Example
# #
# # # 1.add two numbers
# a=lambda a,b:a+b
# print(a(12,12))
#
# # # 2.multiply two numbers
# b=lambda a,b:a*b
# print(a(10,20))
#
# # 3.find maximum of two numbers
# m=lambda a,b:max(a,b)
# print(m(10,23))
#
# # 4.find minimum of two numbers
# mi=lambda a,b:min(a,b)
# print(mi(23,10))# 5.square of a numbers
# l=lambda a:a**2
# print(l(4))
# # 6.cube of a numbers
# cube=lambda c:c**3
# print(cube(12))
# #
# # 7.check even number
# c=int(input("enter the number"))
# number=lambda i:f"the number is even{c}" if c%2==0 else f"the number is odd"
# print(number(c))
# # 8.Absolute valu
#
# #a=lambda
# # 9.greater among three numbers
#
# am=lambda i,j,K:max(i,j,K)
# print(am(12,11,23))
#
# # 10.length of a string
# enter="Enter the String"
# a=lambda i:len(i)
# print(a(enter))
# # 11.Reverse  string
# b="Reverse"
# a=lambda b:b[::-1]
# print(a(b))
#
# # 12.Palindrome check
# polindrome=lambda s:s==s[::-1]
# print(polindrome("mom"))
# 13.find largest word in a string
# s="python is powerful"
# larges=lambda s:max(s.split())
# print(larges(s))
#
# # 14.Last digit of a number
# s=789
# digit=lambda s:s%10
# print(digit(s))
# #
# 15.First digit of a number
# s=789
# m=lambda i: int(str(i)[0])
# print(m(s))
#
# 16.Swap two numbers
# a=10
# b=20
# swap= lambda z,x:(x,z)
# print(swap(a,b))
#
# 17.Leap year check
# s=2025  or s=2024
#
# leap=lambda y:y%4==0
# print(leap(2025))
# print(leap(2026))

# 18.String uppercase
# x="python"
# upper_case=lambda u:u.upper()
# print(upper_case(x))


# 19.Title case string
# y="hello world"
# t=lambda h:h.title()
# print(t(y))

# 20.Count words in a string
# s="python is great"
# count=lambda l:len(l.split())
# print(count(s))

# v=lambda s:len(s.split)
# print(v(s))
# 21.wap to check the number is divisible by both 3 and 7

l=lambda a:f"the is divisible {a}" if a%3==0 and a%7==0 else f"the number not divble {a}"
print(l(21))




# 22.Square root of a number
# y=lambda  d:d**0.5
# print(y(18))

# 23.Rectangle area (length * width)
# area= lambda  l,w:(l*w)
# print(area(12,32))
#
# 24.Circle area (pi*r*r)
# circle_area=lambda r:(3.14*r*r)
# print(circle_area(10))

# 25.Concatenate two strings
c="the class is python  "
t="this class time in 5:30pm "
Concatenation=lambda a,b:a+b
print(Concatenation(c,t))

# 26.Repeat string n times
# n=input()
# s=lambda d:d*5
# print(s(12))
# print(s("hii"))
# 27.Check substring present
# substring=lambda sub,s: sub in s
# print(substring("powerful","python is powerful languages"))

# 28.Find the largest of four numbers(use max()function)
# largest=lambda a,b,c,d:max(a,b,c,d)
# print(largest(12,11,34,12,))
#
# # 29.wap to return the key of a dictionary
# a={"hello":"Sony","How":"are","you":"bye"}
# w=lambda r:r.keys()
# print(w(a))
# # 30.wap which returns first element of a sequence
# # first=lambda sequ:sequ[0]
# # print(first([12,10,20,30,50]))
# # 31.wap which returns length of any iterable
# # s=lambda d:len(d)
# # print(s([1,23,45,67,8]))
# # 32.wap which returns the list of squares of numbers in a list
# l=[4,5,6,2,3,1]
# number=lambda k:list(map(lambda x:x*x,l))
# print(number(l))
#
# # 33.wap to print the numbers present in a list with their corresponding indices pair
# # l=[100,200,300,400,500]
# # pri=lambda k:list(enumerate(l))
# # print(pri(l))
#
#
#
# # 34.wap to check a data is sequence if it is sequence then return length pair else type pair
#
# check_seq=lambda  x:("length",len(x))if hasattr(x,"__len__")else("type",type(x))
# check_seq("python")
# check_seq(123)
# # 35.wap to check even or odd,if it is even return square of that value else square root of that
# value=lambda m: m**2 if m%2==0 else math.sqrt(m)
# print(value(12))
# print(value(7))
# #
# # 36.wap to check len of given string ,if length is even return as it is else return reverse
# # of that string
# string2=lambda l:l if len(l)%2==0 else l[::-1]
# print(string2("the name of string is pytho"))
# print(string2("the name of string is pytho"))
# # 37.wap to check length of given string and return value and length in tuple and dictionary
# # t=lambda y:(y,len(y),{y:len(y)})
# # print(t("the nae is jagtap nimbraj"))
#
# # 38.wap to check a data is sequence if it is sequence then return length pair else type pair
#
# check=lambda m:({m:m**2} if isinstance(m,(int,complex,float,bool)) else type(m))
# check = lambda m: ({m: m**2} if isinstance(m, (int, float, complex, bool)) else type(m))
# print(check(12))
# print("the number is even and odd")
# # 39.wap to return if no is divisible by 5 then increment with 5 else decrement with 5
# y=lambda d:d+5 if d%5==0 else -5
#
# print(y(12))
# print(y(10))
#
# # 40.Check if string is an anagram
# # s="listen"
# # s1="silent"
# # d=lambda s,s1:sorted(s)==sorted(s1)
# # print(d(s,s1))