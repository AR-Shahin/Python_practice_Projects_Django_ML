class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DobelyList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.count = 0

    def lengthOfList(self): return self.count

    def insert(self, data):
        newNode = Node(data)

        if self.__tail is None:
            self.__head = newNode
            self.__tail = newNode
            self.count += 1
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
            self.count += 1

    def insertFirst(self, data):
        newNode = Node(data)
        temp = self.__head
        temp.prev = newNode
        newNode.next = temp
        self.__head = newNode
        self.count += 1

    def insertAtPosition(self, pos, data):
        if(pos == 1):
            self.insertFirst(data)
        elif pos == self.lengthOfList():
            self.insert(data)
        else:
            index = 1
            temp = self.__head
            while pos > index:
                index += 1
                temp = temp.next
            newNode = Node(data)
            newNode.prev = temp
            newNode.next = temp.next
            temp.next = newNode
            newNode.next.prev = newNode
            self.count += 1

    def print_list(self):

        temp = self.__head

        while temp is not None:
            print(temp.data)
            temp = temp.next

    def deleteFirst(self):
        temp = self.__head
        self.__head = temp.next
        # temp.next = None
        self.count -= 1
        del temp

    def deleteLast(self):
        temp = self.__tail
        self.__tail = self.__tail.prev
        self.__tail.next = None
        self.count -= 1
        del temp

    def deleteAtPosition(self, pos):
        if pos == 1:
            self.deleteFirst()
        elif pos == self.lengthOfList():
            self.deleteLast()
        else:
            index = 1
            temp = self.__head
            while pos > index:
                index += 1
                temp = temp.next
            temp.prev.next == temp.next
            temp.next.prev = temp.prev
            self.count -= 1
            del temp


db = DobelyList()
db.insert(10)
db.insert(100)
db.insert(1000)
db.insert(10000)
db.print_list()
db.deleteAtPosition(3)
db.deleteAtPosition(3)
# db.deleteFirst()
# db.deleteFirst()
print('-------------')
# db.insert(5000)
db.print_list()
