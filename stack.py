class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        if self.items == []:
            print "True - stack is empty"

        else:
            print "False - stack is not empty"

myStack = Stack()
item = raw_input("Enter the Number for input = ")
myStack.push(item)

choice = raw_input("Want to pop for stack (Y/N)")
if choice is "Y" or choice is "y":
    myStack.pop()

myStack.isEmpty()
