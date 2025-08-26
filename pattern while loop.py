# # python using Right-Angled  triangle
# user=int(input("enter the number---> "))
# i=1
#
# while i<=user:
#     j = 1
#     while j<=i:
#         print("*", end=" ")
#         j=j+1
#     print()
#     i=i+1
#### Inverted Right-Angled Triangle
# user=int(input('Enter the number-->'))
# while user > 1:
#     j=1
#     while j < user:
#         print("*", end=" ")
#         j+=1
#     print()
#     user-=1


#### pyramid pattern
# n=int(input("Enter the number---> "))
# i =1

# while i<= n:
#     s=1
#     while s <=n-i:
#         print(" ",end=" ")
#         s=s+1
#     j=1
#     while j<=(2*i-1):
#         print("*",end=" ")
#         j+=1
#
#     print()
#     i=i+1

  # dereasing triangle pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="")
#     print()


#### right sided triangle
# user=int(input("Enter the number--> "))
# for i in range(user):
#     for j in range(i,user):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print

# # hii pattern
# user=int(input("Enter the number--> "))
# for i in range(user):
#     for k in range(user-i-1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#
#     print()

# # reverse hii pattern
# user=int(input("Enter the number-->  "))
# for i in  range(user,0,-1):
#
#     for j in range(user-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" * ",end=" ")
#
#     print()
#

#
# ### diamond pattern
# Diamond Pattern
# Diamond Pattern
# user = int(input("Enter the number: "))

# Upper pyramid
# for i in range(user):
#     # spaces
#     for j in range(user - i - 1):
#         print(" ", end=" ")
#     # stars
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()
#
# # Lower pyramid
# for i in range(user - 2, -1, -1):
#     # spaces
#     for j in range(user - i - 1):
#         print(" ", end=" ")
#     # stars
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()
