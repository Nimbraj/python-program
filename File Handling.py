## os MODUALE
## TO Perform file operation/handling we user a methods in OS
# Module that is
# 1.getcwd
# it stand for "current working directory"
# import os
#
# a=["good",45,[1,21],78.6,(4,5),8+7j,(9,7),False,{"a":75}]
# os.getcwd()

# 2.chdir():

  # it stands for directory.
  # it will change  path ?location from current to specified
# location/path

  # Syntax =os.chdir("path")

## popen()
# this method is used open a file /pop up a file
# syntax :- os.popen("file_name")

## 4.
    # mkdir
## it stands for  method
     # is used to create a directory a specified location /path
     # it will throw an error if we create a directory  which already exist
     # syntax os.mkdir ("directory_name")

## 5.
  # rmdir
  #### it stands for "remove directory"
  # this methods is used to remove the directory from specified location and path

## 6.
   # remove()
   #   this methods is used to remove a file (any kind of file)
   #   syntax
   #   os.remove()

###7.
   # listdir
   ## it is stands for list directory
   # it will return a list  of file any directory present in a specified location /path.
   # syntax
   # os.listdir
##8
 #os.path.exists()
   ### it will return ture if the specified path exits it will return false
   # syntax
   ## os.path.exists()
## 9
 # rename()
  # this method is used to rename a file
  # syntax os.return ("old value","new value")

# import os
 # example on getcwd
# print(os.getcwd()) crrent location


 # chdir
# os.chdir(r'C:\Users\Admin\PycharmProjects')
# print(os.getcwd())


# os.chdir(('C:\Users\Admin\PycharmProjects\Python\File Handling'))
# print(os.getcwd())
#
#
#
# ## example on popen
# os.chrdir(r"E:/mrng_file")
# os.popen("demo.text")
# os.poppen("pic.png")
#
# os.mkdir("afternoon")

#example on rmdir()
# os.chdir(r"E:\mrng_file")
# os.rmdir("mon")
# os.rmdir("sample.txt")
# os.chdir(r"E:\mrng_file")
# os.rmdir("mon")
# FileNotFoundError: [WinError 2] The system cannot find the file
# specified: 'mon'
#example on remove()
# os.chdir(r"E:\mrng_file")
# os.remove("sample.txt")
# os.remove("pic.png")


  ############# file ##########
# A file is a collection of data /a group of information is called a file .
#  each file will be identified by its own extensin.


# file  operation:
#   there are 4 file operation  that  are
      ### read  --->r
      ## write  -->w

      ## append ---> a
      ## create -->x

# *"r" is a default mode in all the file
#it means we can just read a file but we can't write
# anything inside a file

# *'w'-->write
# when we want to write anything inside a file then we go 'w' mode
## it will override old data ,meaning old data will be removed
# and new data will be written

 # a---> append

# when we want append something into an existing file then we go 'a ' mode
# it will keep old data and it will add new data in a file


 # x-> create
# "When we want to create a new file we use 'x mode
# to perform any file operation  we need to open a file to open file we use a method called 'open()'   method




# opening a file in python there are 2 way
# 1.without context manager :
# in this syntax we shold manually close the file
# syntax
# var_name = open ("file_name","mode")



# with context manager:
# in this syntax we shoud manually close the file
# of the block
# syntax
# with open("file_name","mode")as var_name:
#
# import os
# print(os.getcwd())
# file=open("joy.text",'x')
# print(file.mode)
# print(file.name)
# file.close()
# file=open("joy.text",'r')
# print(file.read())


##  How to create empty class
