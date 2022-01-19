

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertLast(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = self.tail = newNode
            self.count += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.count += 1

    def insert_first(self, data):
        if self.head is None:
            self.insertLast(data)
        else:
            newNode = Node(data)
            temp = self.head
            temp.prev = newNode
            newNode.next = temp
            self.head = newNode
            self.count += 1

    def insert_at_position(self, pos, data):
        list_length = self.length_of_list()
        if pos <= 0:
            print("Invalid Position")
            return
        if pos == list_length + 1:
            self.insertLast(data)
            return
        if pos == 1:
            self.insert_first(data)
            return
        if pos <= list_length:
            index = 1
            temp = self.head
            while index != pos:
                index += 1
                temp = temp.next

            prevNode = temp.prev
            newNode = Node(data)
            newNode.prev = prevNode
            newNode.next = temp
            temp.prev = newNode
            prevNode.next = newNode
            # print(index, pos, temp.data, prevNode.data)
            return
        else:
            print("Out of Range!!")
            return

    def length_of_list(self):
        return self.count

    def print_list(self):

        temp = self.head

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def print_reverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1
        return

    def delete_last(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1

        return

    def delete_at_position(self, pos):
        list_len = self.length_of_list()

        if pos <= 0 or list_len < pos:
            print("Invalid Position!!")
            return
        if pos == 1:
            self.delete_first()
        if pos == list_len:
            self.delete_last()

        index = 1
        temp = self.head
        while(index != pos):
            temp = temp.next
            index += 1

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.count -= 1
        return

    def max_value(self):
        list = []

        temp = self.head
        while temp is not None:
            list.append(temp.data)
            temp = temp.next
        return max(list)


ob = LinkList()
ob.insertLast(10)
ob.insertLast(20)
ob.insertLast(30)
ob.insertLast(40)
# ob.insertLast(40)
# ob.insert_first(100)
# ob.insertLast(40)
ob.print_list()
# print(ob.length_of_list())
# ob.insert_at_position(2, 40)
# ob.insertLast(50)
# ob.delete_at_position(2)

# ob.print_list()
# ob.print_reverse()

print(ob.max_value())
