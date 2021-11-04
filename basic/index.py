
def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True


# num = int(input("Enter a Number : "))

# if(isPrime(num)):
#     print(f"{num} is a Prime Number")
# else:
#     print(f"{num} isn't Prime Number")

x = 10
# print(type(x))
multiStr = "   My name is Shahin"
split = multiStr.strip().split(" ")

# print(split)

myList = ['Shahin', 101, True]

# print(myList)

# myList.append(10)  # Insert value in last position

# myList.insert(2, 'Omi')  # Insert a Position
# print(myList)
# newList = [10, 20, 30]
# myList.extend(newList)  # extend another list

# # myList.remove('Shahin') # Remove

# myList.pop(1)
# print(myList)

# myList.clear()

# print(myList)

# if 'ad' in 'shahin':
#     print('ok')
# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)


def x(a): return a + 10


# def myfunc(n):
#     return lambda a: a * n


# mydoubler = myfunc(2)

# print(mydoubler(11))


def print_dictionary(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print_dictionary(value)
        else:
            print(f"{key} => {value}")


def singleDic(dic):
    for i, j in dic.items():
        print(i)


dic = {
    'name': 'Shahin',
    'age': 22,
    "degree": {
        "hmc": 'A+',
        "address": {
            'Area': 'Hajigonj'
        },
        "SEU": 3.88
    }
}
dic.update({'address': 'Dhaka'})
# print(dic.items())
print_dictionary(dic)

with open("./assets/input.txt", mode="r") as file:
    words = []
    for line in file.readlines():
        newLine = line.strip().split(" ")
        words += newLine
    # print(set(words))
