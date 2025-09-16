

## Adding element to a dictionary
# 1.key - value syntax
# 2.update
#3. set default
#4.from keys
            ##### 1. key -value syntax
            # dict[new key]= value
# fam ={ "davanagere":"glass house","mysore":"palace"}
# fam["jaipur"]="hawa mahal"
# print(fam)
#
#
# # ####update#########
# #     syntax:
# #        dict.update({key:value})
# # update examples
# a={1:2}
# a.update({"a":9})
# print(a)
# p={"banglore":57001,"kalaburagi":4334 ,"jaipur":302001 }
# p.setdefault("dawanagere",577004)
# p.setdefault("Nannaj",413205)
# p.setdefault("deccan")
#
# print(p)
#
# #4. fromkeys():
# a="hello"
# print(dict.fromkeys(a))
#
#
#  # removing elements from A dictionary
#  # pop()
#
#
# ## count frequency of element
# arr=[1,2,1,2,3,1,2]
# freq=()


# arr=[1,2,2,3,1,1,4,2,]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)
#  swap key and value
# d={'a':1,'b':2,'c':3}
# swaped={v:k for k ,v  in d.items()}
# print(swaped)



# # checked if two dictionary are equal
# d1={'a':1,'b':2}
# d2={'b':2,'a':1}
# print(d1==d2)
       # # Merge two dictonaries and value
# d1={'a':10,'b':20,'c':30}
# d2={'a':40,'b':40,'d':60}
# merged=d1.copy()
# for k,v in d2.items():
#     merged[k]=merged(k,0)+v
# print(merged)

#
# # find key with maximum value
# d={'a':100,'b':200,"c":50}
# max_key=max(d,key=d.get())
# print(max_key)
#
#
# # revome the duplicate value
# d={'a':1,'b':2,'c':1,'d':3}
# unique={}
# for k,v in d.items():
#     if v not in unique.values():
#         unique[k]=v
# print(unique)
#

 # Group words by first letter
# words=['apple','banana','apricot','cherry','blueberry']
# grouped={}
# for word in words:
#     first = word[0]
#     grouped.setdefault(first.append(word))
# print(grouped)

 # sort dictionary by value
d={'a':3,'b':1,'c':2}
asc=dict(sorted(d.items(),key=lambda x:x[1]))
des=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print("Ascending:",asc)
print("descending :",des)





# convert two list into dictionary (ignore duplicate)
# keys=['a','b','c','d','a']
# value=[1,2,3,45,]
# d={}
# for k,v in zip (keys ,value):
#     if k not in d:
#         d[k]=v
# print(d)

# fatten nested dictonary
# def fatten(d,p_key=,spe=):
# d1={"a":1,'b':2,'c':3,"d":4}
# d2={'b':10,'c':20,'e':30,"f":40}
# m= d1.copy()
# for k ,v in d2.items():
#     m[k]=m.get(k,0)+v
# print(m)
# class Library:
#     def __init__(self):
#         self.book={}
#     def add_book(self, name ,price):
#         if name in self.book:
#             print(f"{name} is already present in the library ")
#         else:
#             self.book[name]=price
#             print(f"Book {name} added with price {price}.")
#     def update_price( self, name, price):
#         if name in self.book:
#             print(f"price of {name} update to price{price}")
#         else:
#             print(f"{name} is  not available in the library")
#     def display_book(self):
#         """Display all book with price"""
#         if not self.book:
#             print("no book in the library")
#         else:
#             print("Book in the library :")
#             for name ,price in self.book.items():
#                 print(f"{name}: Rs{price}")
# Lab=Library()
# Lab.add_book("Python Basics",300)
# Lab.add_book("Data Structures",450)
# Lab.add_book("Python Basics",300)
# Lab.update_price("Data Structures",500)
# Lab.update_price("Machine Learning",800)
# Lab.display_book()

# Create a Python class Subscribe to maintain
# subscriber counts for each hour of the day. Use a
# dictionary where: Key = Hour (e.g., 1, 2, 3 …)
# Value = Number of subscribers at that hour. The
# class should have the following methods:
#     1. add_hour(hour, subscribers) If the hour is
#     not present, add it with the given number of
#     subscribers. If the hour is already present,
#     update it by adding the new subscribers to the
#     existing subscribers.
#     2. total_subscribers() Display the total number of subscribers across all hours
#     . 3. subscribers_in_hour(hour) Display the number of subscribers for a particular hour.
#     If the hour
# is not present, display an appropriate message.
#
# class Subscribe:
#     def __init__(self):
#         self.subscribres={}
#         # dictionary to maintain hour: subscriber_count
#
#     def add_hour(self,subscribes,hour):
#         if hour in self.subscribres:
#             self.subscribres[hour]+=subscribes
#         else:
#             self.subscribres[hour]=subscribes
#
#     def total_subscribers(self):
#         return sum(self.subscribres.values())
#     def subscribers_in_hour(self,hour):
#         if hour in self.subscribres:
#             return f"subscrible in hour{hour}:{self.subscribres[hour]}"
#         else:
#             return f"No data available for hour{hour}"
# A=Subscribe()
# A.add_hour(1,50)
# A.add_hour(2,30)
# A.add_hour(1,20)
#
# print("Total subscribers : ",A.total_subscribers())
# print(A.subscribers_in_hour(1))
# print(A.subscribers_in_hour(3))
#


#
# Write a Python program to reverse a given number. While reversing,
# if any digit is 0, replace it with 5. Do not use string operations.
# Example Input/Output: Input: 1020 Output: 5201 Input: 8090 Output: 5908
#
# def reverse_replace(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         if digit ==0:
#             digit = 5
#         rev =rev * 10 +digit
#         num //=10
#     return rev
# num= int(input("Enter a number:  "))
# print("Output : ", reverse_replace(num))