import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZNOYpRssSr",
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE my_first_db")






