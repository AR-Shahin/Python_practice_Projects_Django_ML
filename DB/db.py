import mysql.connector


class Database:
    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="py_sms"
        )
        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()


class Student(Database):

    def all_students(self, mode='DESC'):
        sql = "SELECT * FROM students ORDER BY id {}".format(mode)

        try:
            my_cursor.execute(sql)
            result = my_cursor.fetchall()
        except Exception as e:
            return e

        return result

    def insert(self, data):

        sql = "INSERT INTO students (name,roll,address) VALUES (%s , %s, %s)"

        try:
            my_cursor.execute(sql, data)
        except Exception as e:
            return e

        return my_cursor.lastrowid

    def insert_many(self, data):
        sql = "INSERT INTO students (name,roll,address) VALUES (%s , %s, %s)"

        try:
            my_cursor.executemany(sql, data)
        except Exception as e:
            return e

    def delete(self, id):
        sql = "DELETE FROM students WHERE id = {}".format(id)

        try:
            my_cursor.execute(sql)
        except Exception as e:
            return e

    def update(self, id, data):

        # sql = "UPDATE customers SET name = %s,roll = %s,address = %s WHERE id = {}".format(
        #     id)
        sql = "UPDATE students SET name = %s ,roll = %s, address = %s WHERE id = {}".format(
            id)

        val = (data[0], data[1], data[2])

        try:
            my_cursor.execute(sql, val)

        except Exception as e:
            return e

    def truncate(self):

        sql = "TRUNCATE TABLE students"
        try:
            my_cursor.execute(sql)
        except Exception as e:
            return e

        return True


db = Database()
st = Student()


# sql = "INSERT INTO students (name, roll,address) VALUES ('kabir',505, 'India')"

# print(db.insert(sql))
# print(st.all_students())
# print(st.insert(('Omi', 1032, 'Dhaka')))
# print(st.truncate())

data = [
    ('Shahin', 101, 'Chandpur'),
    ('Asik', 102, 'Pabna'),
    ('Tanzim', 105, 'Sylhet'),
    ('Nasif', 103, 'Cumilla'),
]

# st.insert_many(data)

print(st.all_students())

# st.delete(5)

st.update(4, (
    'Tanzim',
    1110,
    'Dhaka'
))
print(st.all_students())
