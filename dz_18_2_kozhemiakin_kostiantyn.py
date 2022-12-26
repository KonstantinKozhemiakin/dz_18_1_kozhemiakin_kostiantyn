import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZNOYpRssSr",
    database="my_first_db"
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE students (id INT (10), name VARCHAR(255))")
