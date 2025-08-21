
even =[]
odd= []

for i in range(21):
    if i%2==0:
        even.append(i)
        print(even)
    elif i%2==1:
        odd.append(i)
        print(odd)


from xml.dom.minidom import Element

s="hello123"

for i in range(len(s)):
    if s[i] in 'AEIOUaeiou':
        print(s[i])
    elif s[i].isdigit():
        print(s[i])

# 3.wap to capitalize only the first letter of
# every word in the given list
l=["vaidegi","rahul","shivam","kapil","patil"]
for i in l:
    print(i.capitalize())
# 4.wap to extract only individual data types form
# # the list
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
for i in l:
    if isinstance(i,(int,float,complex,bool)):
        print(i)

# 5.wap to extract only individual data types from
# the list and sum all the individual data types
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
sum=0
for i in l:
    if isinstance(i,(int,float,complex,bool)):
        sum=sum+i
        print(sum)


# 6.wap to print the count of alphabets and numbers
# and space in the given string
s = "india got the independence in the year 1947"

# Counters
alphabets = 0
digits = 0
spaces = 0

# # Loop through each character
for ch in s:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

# Print results
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)

alphabets=0
digits =0
spaces=0
for i in s:
    if i.isalpha():
        alphabets=alphabets+1
    elif i.isdigit():
        digits=digits+1
    elif i.isspace():
        spaces=spaces+1
print(f" alphabete {alphabets}, digit {digits}, spaces {spaces}")




           ######## while loops ####
# # 1.wap to print series of 20 natural numbers
i=0
while i<=20:
    print(i,end=" ")
    i=i+1



# ##### 2 .wap to print series of upper case character
i=65
while i<=97:
    print(chr(i),end=" ")
    i=i+1

# # 3 wap to print series of lower  case character
i=97
while i<123:
    print(chr(i),end=" ")
    i+=1

# # 4 wap to print both upper and lower case character

i=65
j=97
while i<=96 and j<=123:
    print(chr(i),chr(j),end=" ")
    i+=1
    j+=1

## wap to print series of event number till 20 in reverse order
i=20
while i>0:
    print(i ,end=" ")
    i = i - 1



# ########## wap to count numbers of occurrent of specified element in collection
# s = "Hello guys Good morning python is a programming"
#
element = input("Enter the character to count: ")

i = 0
count = 0

while i < len(s):
    if s[i] == element:
        count += 1
    i += 1

print(f"The character '{element}' occurs {count} time(s) in the string.")


#   ##### wap to print even positional character in the given string
#
# ### wap to print the number table by using data given by user
# # (take user input)
a=int(input("enter yor number---> "))
i=1
while i<=10:
    b=a*i
    print(f"{a} * {i}= {b}")
    i+=1




#   #### wap to print the names only if the length of the names is even
l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
i=0
while i<len(l):
    if len(l[i])%2==0:
        print(l[i])
    i=i+1



# ### wap to print the name which is starting with vowel in the given list
names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
i=0
while i<len(names):
    if names[i][0]in ("oueaiOUIAE"):
        print(names[i])
    i=i+1

#
# ###  wap to print sum of numbers in the list


# #### wap to extract only vowels and digits from the give string
s="hellopython123"
i=0
while i<len(s):
    if s[i] in ("oiueaAEUIO"):
        print(s[i])
    elif s[i].isdigit():
        print(int(i))

    i+=1
  #### wap to iterate inside the list check if it having nested list if
#     # yes marge
st1 = ["hello", 11, 20, 55, True, False, "hai", "bye", ["False", "goodnight", "enjoy the holiday"]]

i = 0
new = []   # should be a list, not 0

while i < len(st1):
    if isinstance(st1[i], list):   # check if element is a list
        print("Nested list found:", st1[i])
        new.extend(st1[i])   # merge nested list into new
    else:
        new.append(st1[i])   # add normal elements
    i += 1

print("Merged List:", new)





