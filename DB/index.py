import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_sms"
)
my_cursor = my_db.cursor()
# sql = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), roll INT, address VARCHAR(255))"
# sql = "INSERT INTO students (name, roll,address) VALUES (%s,%s, %s)"
# # val = [
# #     ("Omi", 10, "Dhaka"),
# #     ("Shahin", 30, "Chandpur"),
# #     ("Asik", 40, "Pabna"),
# #     ("Tanzim", 50, "Dhaka"),
# # ]
# val = ("Tamanna", 101, "Dhaka")
# # single sql excute
# my_cursor.execute(sql, val)

# Multiple SQL excute
# my_cursor.executemany(sql, val)
# my_cursor.execute("TRUNCATE students")
sql = "SELECT * from students WHERE address = 'Dhaka' ORDER BY id DESC"
my_cursor.execute(sql)
result = my_cursor.fetchall()

my_db.commit()
for item in result:
    print(item)

# print(my_cursor.rowcount, "record inserted.")
# print("Last inserted Id is ", my_cursor.lastrowid)
