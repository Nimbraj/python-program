
# /d number    /D not number
# /s space    /S not BSPACE
# /w all charters /W not all chatracters

# import re

# x="asdsdfgnmfd"
# y=re.findall('[asb]',x)
# print(y)
#
# r="python class"
# u=re.findall("^python",r)
# print(u)
# u1=re.findall("class$",r)
# print(u1)
e="qwertyuioplkjhgfdsazxcvbnmasd7654234567sdds6543sdfg"
# r=re.findall(r"[0-9]{4}",e)
# print(r)

# 1.matches any number between 0-9
# import  re
# a="the cost of the book is Rs.100 "
#
# A=re.findall("[0-9]",a)
# print(A)


# 3.write a program to count the number white space in give string
# import  re
# c="hello world welcome to python hi how are you. hi  how are you"
# a=re.findall("[ ]",c)

# REGULAR
# EXPRESSION
# EXAMPLE

# # 1.matches any number between 0-9
# import  re
#
# a = "The cost of the book is Rs.100"
# b=re.findall("[0-9]",a)
# # 2.matches only lower case letter and upper case letter
# b = "hello HOW ARE YOU"
# B=re.findall("A-Z",b)
#
# # 3.write a program to count the number of white space in a given string
# c = "HELLO world welcome to python Hi how are you. Hi how are you"
# a= re.findall(" ",c)
# print(len(a))
#
# # # 4.sum all the numbers in the below string
# word = "PYTHON12nREG567exp2"
# l=re.findall("[0-9]",word)
# print(l)
# #
# # # 5.matches everything apart from numbers between 0-9
# a = "The cost of the book is Rs.100"
# l=re.findall("[0-9]",a)
# print(l)
# #
# #
# # # 6.matches everything apart from "a","b","c","d"
# b = "abcdefghijklmnop"
# z=re.findall("[abcd]",b)
# print(z)
# # 7.matches only those characters accepts digit# word = "@hello12world34welcome!123"

#
# # 8.extracting file with extension
#
# s = "Downloading http://archive.zip file to download folder python http://hero.py and afternoon.txt and slicing.jpeg"
#
# # 9.wap to extract only pincode
#
# s = "Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
#
# # 10.wap to print the AADHAR CARD numbers
#
# s = "my aadhar number is 1234-4567-8910"
#
# # 11.wap to print thepan card number
#
# a = "my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
#
# # How to fetch the protocols
# a = "https://www.google.com"
#
# # o / p - -->['https', 'www', 'google', 'com'](i
# # want first output like this )
# # o / p - -->['https://www.google.com'](
#
#
# # 13. creating acronyms of the file format
#
# file_format = ["Graphic Interchange Format",
#                "Advanced Audio Coding",
#                "HyperText Markup Language",
#                "Content Management System",
#                "Windows Media,Audio",
#                "Comma Separated Values"]
#
# # o / p -->GIF, AAC, HTML, CMS, WMA, CSV
#
# # 14. wap to match email ids
#
# emails = ["mailto:test.user@company.gov"mailto:, "test_user@company.edu"
# mailto:, "123test-T.user@company.in", "testing@company"
# mailto:, "pspider@company.in"]
#
#
#
#
# # 15. matching phone numbers
#
# phonenumbers = ["123-345-0987", "456-9832-098", "800-987-4756", "080-1029384727", "123-345-12", "900-938-0987"]
#
# # 16. replace whitespace with newline characters
#
# s = "helloworld welcome to python"
#
# # 17.replace all digits with **
#
# s = "hello 123 mic testing 123 123"

#
# ext="improtant date:25-12-2025,2025/09/11,01,january2023"
# import re
# # match=re.findall(r"\d{2}-\d{2}-\d{4}|\d{4}\d{2}-\d{2}|\d{2}-\s[a-z]-\d{4}",ext)
# y=re.findall(r'\\+[0-9]+\\d+\\w',ext)
# print(y)
# # print(match)



# # import re
# #
# # a="Apple123@gmail.com"
# # w=re.findall("[A-Za-z0-9@]+\\.[a-zA-z]+",a)
# # print(w)
#
#
# s="helloworld welcome to python"
# r= re.sub(" ","\n",s)
# print(r)
#
# #============================================================================================================================================================================================
