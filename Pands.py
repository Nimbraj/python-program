# from loops import count
# #
# # s="python"
# # for i in range(0,len(s)):
# #     print(i,s[i])
# # P="python is dynamic type genral  perpose languages i it is used to wed development and data Analysis data scince and Al Ml  "
# # for i in enumerate(P):
# #     print(i)
# # l=["amazon","flipkart","ebay","insta","twitter","meta"]
# # for i in enumerate(l):
# #     print(i)
#
# #
# # for i in reversed(l):
# #     print(i)
#
# # for i in sorted("the is most popular dis in india are the best by sotred is an inbuilt function which is used to sort any iterable "):
# #     print(i,end="")
#
#
# # zip:isc  an inbuilt class ,which is
# # basically is used  to group /pair same index element from the give iterable
# # from itertools import zip_longest
# # a=[10,50,23,89,11,11,22,1]
# # b=[78,3,82,13,11]
# # for i in  zip(a,b):
# #     print(i)
# # for i in zip_longest(a,b):
# #     print(i)
# # s="hello123"
# # for i in s:
# #    if i.isalpha():
# #        print(i,end="")
# #
# # l=["viadegi","rahul","shiv","kapil","patil"]
# # for i in l:
# #     print(i.title(),end="")
# # l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# # for i in l:
# #     if isinstance(i,(int, float,complex,bool)):
# #         print(i,end="")
#
#
# s="india got the independence in the year 1947"
# for i in s:
#     if i.isalpha():
#         print(s.count(i))
#
# from module import fibbo
# print(fibbo(11))
# from module import reverse
# print(reverse(12321))
#
# from module import prime
# print(prime(15))
# from module import factorail
# print(factorail(5))


# def reverse(num):
#     rev=0
#     chek=num
#     for i in num:
#         digit=num %10
#         rev=rev*digit+10
#         digit//=10
#     if num == chek:
#         print(f"the are {num}")
#     else:
#         print(f"not are {num}")
# print(reverse(12))
#
# def factorial(num):
#     return 1 if num==0 else num*factorial(num-1)
# print(factorial(5))
def prime(num):
   count=0
   for i in range(1,num):
       if num%i==1:
           count+=1

   if count==2:
       print(f"the is number is prime {num}")
   else:
     print(f"this number is not prime{num}")
prime(12)