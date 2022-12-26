import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZNOYpRssSr",
    database="my_first_db"
)

my_cursor = mydb.cursor()

insert_name = ''' INSERT INTO students (name) VALUES ('John') '''
my_cursor.execute(insert_name)
mydb.commit()

add_info_in_employee = "INSERT INTO employee (name, salary) VALUES (%s,%s)"
val = [
    ('John', '10000')
]
my_cursor.executemany(add_info_in_employee, val)
mydb.commit()
