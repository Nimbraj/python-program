# PYTHON DATABASE CONNECTIVITY / COMMUNICATION
# drawback of file_handling --> we can perform particulat file
# data present in unstructured format
# security
# storage issue
# only local system we are using

# why we are using pdbc?
# store data in python programing lang


# 1--> python should be install
# 2--> database should be prasent.
# mysql-connector

# import mysql.connector
# host='localhost' / ip address
# / user='root'
# / password='root'


#
# import mysql.connector as mycon
# print("start")
# conn=mycon.connect(
#     host="localhost",
#     user='root',
#     password="root"
# )
# cur=conn.cursor()
# crd="CREATE DATABASE STUDENT"
# print('End')
# if conn.is_connected():
#     print("connection is successfully")
# else:
#     print("connection is not successfull")
