# from collections import deque
# x=deque([1,2,3,4])
# x.append(1)
#
# x=deque([1,2,3,4,5])
# x.rotate(3)
# print(x)
#
#
# import  os
# print(os.getcwd())
# with open("joy.text",'r') as file:
#     new=deque(file,5)
#     print(new)
#


# from itertools import  islice
# with open("joy.text","r")as file:
#     new=islice(file,0,3,1)
#     for i in new:
#         print(i)



import os
with open("joy.text","r") as file:
    print(file.tell())
    print(file)






