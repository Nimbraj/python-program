


# lock :- it will allows only one thread at time .we need to create an object of lock()
# if you want to acquire the lock  the we need to used lock().accuire()
# if you want to release the lock  the we need to used lock().release()
#
# ### drawback- it will blocked our main thread . so we didn't get the output
# it will also not participice
# WHEN WE NEED TO GIVE ACCESS WE CAN USE SEMAPHORE


# from threading import  *
# from time import sleep
# l=Lock()
#
# def printingName(name):
#     l.acquire()
#     l.acquire()
#     for i in range(5):
#         print("thread name is ",name)
#         sleep(1)
#     l.release()
#     l.release()
# t=Thread(target=printingName,args=("sonakshi",))
# t2=Thread(target=printingName,args=("minakshi",))
# t.start()
# t2.start()
## HERE IT WILL BLOCK WE DIDNT GET ANY OUTPUT THAT'S WHY WE ARE USING RLOCK()


# from threading import  *
# from time import sleep
# l=RLock()
#
# def printingName(name):
#     l.acquire()
#     l.acquire()
#     for i in range(5):
#         print("thread name is ",name)
#         sleep(1)
#     l.release()
#     l.release()
# t=Thread(target=printingName,args=("sonakshi",))
# t2=Thread(target=printingName,args=("minakshi",))
# t.start()
# t2.start()

##

# from threading import  *
# from time import sleep
# l=Semaphore(2)
#
# def printingName(name):
#     l.acquire()
#
#     for i in range(5):
#         print("thread name is ",name)
#         sleep(1)
#     l.release()
#
# t=Thread(target=printingName,args=("sonakshi",))
# t2=Thread(target=printingName,args=("minakshi",))
# t.start()
# t2.start()
#INSTEAD OF SEMAPHORE WE CAN USE BOUNDED SEMAPHORE

# from threading import *
# from threading import BoundedSemaphore
# from time import sleep
#
# l = BoundedSemaphore(2)
#
#
# def printingName(name):
#     l.acquire()
#
#     for i in range(5):
#         print("thread name is ", name)
#         sleep(1)
#     l.release()
#
#
# t = Thread(target=printingName, args=("sonakshi",))
# t2 = Thread(target=printingName, args=("minakshi",))
# t.start()
# t2.start()

# IF WE WANT TO ACQUIRE MULTIPLE THREAD
