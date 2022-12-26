import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZNOYpRssSr",
    database="my_first_db"
)

my_cursor = mydb.cursor()
my_cursor.execute("ALTER TABLE students MODIFY id INT AUTO_INCREMENT PRIMARY KEY")
