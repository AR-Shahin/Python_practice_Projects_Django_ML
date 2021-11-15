# Stack Implement using Dobely Linklist
from linklist import DobelyList


class Stack:
    def __init__(self):
        self.__list = DobelyList()

    def push(self, data):
        self.__list.insert(data)

    def pop(self):
        self.__list.deleteLast()

    def peek(self):
        return self.__list.getTail().data

    def print_stack(self):
        temp = self.__list.getTail()
        __list = []
        while temp is not None:
            __list.append(temp.data)
            temp = temp.prev
        print(__list)

    def length_of_stack(self):
        return self.__list.lengthOfList()

    def is_empty(self):
        if self.__list.lengthOfList() == 0:
            return True
        else:
            return False


st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.print_stack()
st.pop()
# st.print_stack()
print(st.length_of_stack())
print(st.peek())

print(st.is_empty())
