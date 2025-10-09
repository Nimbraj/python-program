#
# def fibbo(num):
#     a,b=0,1
#     for i in range(num+1):
#         print(a,end=' ')
#         a,b=b,a+b

# def reverse(n):
#     s=0
#     res =n
#     for i in range(n):
#         digit=n%
#         10
#         s=s*digit+10
#         digit//=10
#     if res == n:
#         print(f'{n} this number is pal')
#     else:
#         print(f' {n} its not pal number')
#
# def prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i==0:
#             count +=1
#     if count ==2:
#         print(f' {num } is prime')
#
#     else:
#         print(f'{num} number is not prime')
def factorail(num):
    return 1 if num==0 else num*factorail(num-1)

