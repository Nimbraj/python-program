#
# # /d number    /D not number
# # /s space    /S not BSPACE
# # /w all charters /W not all chatracters
#
# # import re
#
# # x="asdsdfgnmfd"
# # y=re.findall('[asb]',x)
# # print(y)
# #
# # r="python class"
# # u=re.findall("^python",r)
# # print(u)
# # u1=re.findall("class$",r)
# # print(u1)
# e="qwertyuioplkjhgfdsazxcvbnmasd7654234567sdds6543sdfg"
# # r=re.findall(r"[0-9]{4}",e)
# # print(r)
#
# # 1.matches any number between 0-9
# import  re
# # a="the cost of the book is Rs.100 "
# #
# # A=re.findall("[0-9]",a)
# # print(A)
#
#
# # 3.write a program to count the number white space in give string
# # import  re
# # c="hello world welcome to python hi how are you. hi  how are you"
# # a=re.findall("[ ]",c)
#
# # REGULAR
# # EXPRESSION
# # EXAMPLE
#
# # # 1.matches any number between 0-9
# import  re
#
# a = "The cost of the book is Rs.100"
# b=re.findall("[0-9]",a)
# # 2.matches only lower case letter and upper case letter
# b = "hello HOW ARE YOU"
# B=re.findall(r"\w",b)
# print(B)
#
# # 3.write a program to count the number of white space in a given string
# c = "HELLO world welcome to python Hi how are you. Hi how are you"
# a= re.findall(r" \s",c)
# print(len(a))
#
# # # 4.sum all the numbers in the below string
# word = "PYTHON12nREG567exp2"
# l=re.findall(r"[0-9]+",word)
# sum=0
# for i in l:
#     sum=sum+int(i)
#     print(sum)
#
# # # 5.matches everything apart from numbers between 0-9
# a = "The cost of the book is Rs.100"
# l=re.findall(r"[\d]+",a)
# print(l)
# #
# #
# # # 6.matches everything apart from "a","b","c","d"
# b = "abcdefghijklmnop"
# z=re.findall("[^abcd]",b)
# print(z)
# # 7.matches only those characters accepts digit#
# word = "@hello12world34welcome!1"
# z=re.findall(r"[\s]",word)
# print(z)
# # 8.extracting file with extension
#
# s = "Downloading http://archive.zip file to download folder python http://hero.py and afternoon.txt and slicing.jpeg"
# z=re.findall(r"[\.]",s)
# print(z)
# # 9.wap to extract only pincode
import re
# s = "Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# z=re.findall(r"\b\d+",s)
# y=re.findall(r"\b[0-9]+",s)
#
#
#
# # # 10.wap to print the AADHAR CARD numbers
#
s = "my aadhar number is 1234-4567-8910"
y=re.findall(r"\d{4}-\d{4}-\d{4}",s)
# #
# # file_format = ["Graphic Interchange Format",
# #                "Advanced Audio Coding",
# #                "HyperText Markup Language",
# #                "Content Management System",
# #                "Windows Media,Audio",
# #                "Comma Separated Values"]
# # # o / p -->GIF, AAC, HTML, CMS, WMA, CSV
# # #
# #
# # for i in file_format:
# #     x=re.findall('[A-Z]',i)
# #     print("".join(x))
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # 11.wap to print thepan card number
# #
a = "my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
z=re.findall(r"\w{5}+\d{4}+\w{1}+",a)
print(z)
# #
# # # How to fetch the protocols
# # a = "https://www.google.com"
# #
# # # o / p - -->['https', 'www', 'google', 'com'](i
# # # want first output like this )
# # # o / p - -->['https://www.google.com'](
# #
# #
# # # 10. creating acronyms of the file format
# # #
# # file_format = ["Graphic Interchange Format",
# #                "Advanced Audio Coding",
# #                "HyperText Markup Language",
# #                "Content Management System","Windows Media,Audio", "Comma Separated Values"]
# #
# # # o / p -->GIF, AAC, HTML, CMS, WMA, CSV
# #
# #
# # for i in file_format:
# #     x=re.findall([r'[A-Z]'+,i):
# #     print("".join(x))
#
# # # 14. wap to match email ids
# #
emails = ["test.user@company.gov", "test_user@company.","123test-T.user@company.in", "testing@company"
                     , "pspider@company.in"]
for i in emails:
    m=re.findall(r"[A-Za-z@0-9-.]",i)
    print("".join(m))


for i in emails:
    m=re.findall(r"\w\S",i)
    print("".join(i))
#
# #
# #
# # # 15. matching phone numbers
# # #
# phonenumbers = ["123-345-0987", "456-9832-098", "800-987-4756", "080-1029384727", "123-345-12", "900-938-0987"]
# for i in phonenumbers:
#     p=re.findall(r"\d{3}-\d{3}-\d{4}",i)
#     print("".join(i))
# # # # 16. replace whitespace with newline characters
# # #
# s = "helloworld welcome to python"
# t=re.sub(" ","\n",s)
# print(t)

# #
# # # 17.replace all digits with **
# #
# # s = "hello 123 mic testing 123 123"
#
# #
# # ext="improtant date:25-12-2025,2025/09/11,01,january2023"
# # import re
# # # match=re.findall(r"\d{2}-\d{2}-\d{4}|\d{4}\d{2}-\d{2}|\d{2}-\s[a-z]-\d{4}",ext)
# # y=re.findall(r'\\+[0-9]+\\d+\\w',ext)
# # print(y)
# # # print(match)
#
#
#
# # # import re
# # #
# # # a="Apple123@gmail.com"
# # # w=re.findall("[A-Za-z0-9@]+\\.[a-zA-z]+",a)
# # # print(w)
# #
# #
# # s="helloworld welcome to python"
# # r= re.sub(" ","\n",s)
# # print(r)
# #
# # #============================================================================================================================================================================================









