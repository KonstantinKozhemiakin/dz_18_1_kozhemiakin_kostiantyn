import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZNOYpRssSr",
    database="my_first_db"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, "
                  "name VARCHAR(255), salary INT(6))")
