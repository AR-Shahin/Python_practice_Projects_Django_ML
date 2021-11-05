import camelcase
import json
import helpers as H
import datetime


class Person:

    def __init__(self, name, age: int) -> None:
        self.__name = name
        self.age = age

    def info(self):
        return f"My name is {self.__name}. I am {self.age} years old!"


p1 = Person("Shahin", 22)
# print(p1.info())


class Helper:
    def test(args):
        print("Hello Test")


class Test:
    def test(args):
        print("Hello Test")


class Student(Person, Helper):
    def __init__(self, name: str, age: int, Id=500) -> None:
        self.id = Id
        super().__init__(name, age)

    def get_id(self):
        return self.id
# print(Person.name)


s1 = Student("omi", '22')
# print(s1.info())
# s1.test()

x = 10


def inner():
    global x
    x = 500
    print(x)


# inner()
# print(x)

class ShapeInterface:
    def area(args):
        pass


class Triangle(ShapeInterface):
    def __init__(self, h, b) -> None:
        self.height = h
        self.base = b

    def info(self):
        print(self.height, self.base)


t1 = Triangle(10, 5)
# t1.info()

# H.echo("Hi")

T = datetime.datetime.now()
# print(T.year)
# print(T.strftime("%B"))
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
