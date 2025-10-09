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



# def factorial(num):
#     return 1 if num==0 else num*factorial(num-1)
# print(factorial(5))
# def prime(num):
#    count=0
#    for i in range(1,num):
#        if num%i==1:
#            count+=1
#
#    if count==2:
#        print(f"the is number is prime {num}")
#    else:
#      print(f"this number is not prime{num}")
# prime(12)


# def reverse(num):
#     rev= 0
#     while num >0:
#         digit= num%10
#         rev=rev*10+digit
#         num//=10
#     return rev
# print(reverse(121234))


# def replace_value(num):
#     result=0
#     place=1
#     if num==0:
#         return 5
#     while num >0:
#         digit=num%10
#         if digit==0:
#             digit=5
#         result =result +digit*place
#         num //=10
#         place*=10
#     return result
# n=int(input("Enter the number---> "))
# print(replace_value(n))

# def pal (num):
#     a=num
#     rev=0
#     i=0
#     while i <= num:
#         digit = num%10
#         rev=rev*digit+10
#         num //=10
#         i+=1
#     if num == a:
#         print('pal')
#     else:
#         print('not pal')
# pal(1231)