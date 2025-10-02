# multiTasking :- Executing several task at  the same time is called as multitasking
# Process based multitasking :-Executing  several task simulataneously at the same time where each every task having their own independent process is called as process based multitasking.
        ##### process based is more effiently used in the operating system  based application
from tokenize import endpats

# thread based  multitasking  :- Executing  several task simulataneously at
# the same time where each every their w

# os based application
# development of wed apps


# multithreading
# 1.without using the class

#2.By extending the threading class
# 3. without using extending thread class

sr="([{}])"


import threading
from threading import current_thread

print(threading.current_thread().name)

# set name :- this changes a thread name
# current_thread().setName("jagtap Nimbraj")
# print(f'My name of thread is {threading.current_thread().name}')





# creating thread by extenting thread class

# from threading import *
# class Siddhesh(Thread):
#     def run(self):
#         for i in range(5):
#             print("this person name is Siddesh")
# t=Siddhesh()
# t.start()
# for j in range(4):
#     print("I name is jagtap")

# # creating thread without extending thread class
# from threading import *
# class Vicky:
#     def rashmika(self):
#         print("this is fiancee  of vicky")
# obj=Vicky()
# t=Thread(target=obj.rashmika())
# t.start()
# for j in range(5):
#     print("i am father of vicky")
#
# from threading import *
# import time
# n=[1,2,34,5]
# def double(n):
#     time.sleep(1)
#     for i in n:
#         print("Double of number is",i*2)
# def Square(n):
#     time.sleep(1)
#     for i in n:
#         print("Square of number is ",i**2)
# start=time.time()
# obj=Thread(target=double,args=(n,))
# obj2=Thread(target=double,args=(n,))
# obj2.start()
# obj.start()
# obj.join()
# obj2.join()
#
# end=time.time()
# print("total time taken to execute the program :",end-start)
