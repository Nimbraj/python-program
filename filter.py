# filter()
# filter is inbuit function
# it will remove default value(unwanted data)
# filter it will accept only two argument
# 1) functionName
# 2)Argument(iterable)

#
# # Syntax:-
# # new_variable_name=filter(FunctionName,iterable)
# d=[1,2,3,4,5]
# def fun(i):
#     return i%2==0
# m=map(fun,d)
# print(list(m))
#
# f1=filter(fun,d)
# print(list(f1))
#
# x=lambda i:i%2==0
# print(list(map(x,d)))
#
#
# print(list(filter(x,d)))

d=[-1,-4,-67,-56,88,100,500,300]
# def pos(i):
#     return i>0
# p=filter(pos,d)
# print(list(p))
# m=map(pos,d)
# print(list(m))

# l=lambda  i:i>0
# m=map(l,d)
# print(list(m))
# print(list(filter(l,d)))

'''
'''

#4.Keep Positive numbers
# x=[-5,-2,10,3,7]
# def pos(i):
#     return i>0
# print(list(filter(pos,x)))


#5.Filter Truthy values
s=[0,False,"",None,"Hii",6]
def truthy(i):
    return bool(i)
print(list(filter(truthy,s)))
print(list(map(truthy,s)))


t=lambda i:bool(i)
print(list(filter(t,s)))
print(list(map(t,s)))

#6.Keep strings starting with “a”
words = ["apple", "banana", "avocado", "cherry"]
# def string(i):
#     return i.startswith("a")
# print(list(filter(string,words)))
# print(list(map(string,words)))

# l=lambda i:i.startswith("a")
# print(list(filter(l,words)))
# print(list(map(l,words)))

#7.Keep only digits from a string
s="a1b2c3d4"
# def digi(i):
#     return i.isdigit()
# print(list(map(digi,s)))
# print(list(filter(digi,s)))
# l=lambda i:i.isdigit
# print(list(filter(l,s)))
# print(list(filter(t,s)))
# print(list(map(t,s)))

#8.Keep only alphabets from a string
# s1= "p3y4t5h6o7n"
# def alph(i):
#     return i.isalpha()
# print(list(filter(alph,s1)))


#9.Filter students who passed (marks ≥ 50)
marks = {"Ann": 45, "Ben": 70, "Cat": 55}
# def passed(i):
#     return marks[i]>=50
# print(list(map(passed,marks)))
# print(list(filter(passed,marks)))


# l=lambda i:marks[i]>=50
# print(list(filter(l,marks)))
# print(list(map(l,marks)))

#10.Keep numbers divisible by 3
nums = [3, 6, 8, 10, 12, 15]
def divisible(i):
    return i%3==0
print(list(filter(divisible,nums)))
print(list(map(divisible,nums)))
l=lambda i:i%3==0
print(list(filter(divisible,nums)))
print(list(map(divisible,nums)))

#11.Keep words longer than 4 letters
words = ["cat", "elephant", "dog", "tiger"]

def longer(i):
    if i>=len(words):
        print(i)
print(list(filter(longer,words)))


#12.Keep palindromes
words = ["madam", "python", "level", "world"]


#13.Keep uppercase words
words = ["HELLO", "world", "PYTHON", "code"]


#14.Filter names that end with “n”
names = ["Arun", "Kiran", "Deepak", "Sohan"]


#15.Keep numbers within a range (10–20)
nums = [5, 10, 15, 20, 25]


#16.Filter emails containing “@gmail.com”
emails = ["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"]


#17.Keep tuples where sum > 10
pairs = [(1,2), (5,6), (3,4), (7,8)]


#18.wap to return a list having only flowers
# l=["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"]




