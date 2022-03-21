
# import the required data structure
from pygorithm.data_structures import stack


# create a stack with default stack size 10
myStack = stack.Stack()

# push elements into the stack
myStack.push(2)
myStack.push(5)
myStack.push(9)
myStack.push(10)

# print the contents of stack
print(myStack)

# pop elements from stack
myStack.pop()
print(myStack)

# peek element in stack
print(myStack.peek())

# size of stack
print(myStack.size())
