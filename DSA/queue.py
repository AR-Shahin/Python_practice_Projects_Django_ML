from linklist import DobelyList


class Queue:
    def __init__(self):
        self.__queue = DobelyList()

    def enqueue(self, data):
        self.__queue.insert(data)

    def dequeue(self):
        self.__queue.deleteFirst()

    def print_queue(self):
        self.__queue.print_list()

    def front_value(self):
        pass

    def tail_value(self):
        pass

    def length_of_queue(self):
        return self.__queue.lengthOfList()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.print_queue()
# q.dequeue()
# print('-----------------')
# q.enqueue(60)
# q.print_queue()
print(q.length_of_queue())
