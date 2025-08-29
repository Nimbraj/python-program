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

