class Stack(object):

    def __init__(self):
        self.item = []
        self.top = -1

    def push(self, value):
        if self.top > len(self.item):
            return False

        self.top = self.top + 1
        self.item.insert(self.top, value)

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            return None

    def displaylist(self):
        return self.item


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()
stack.pop()
stack.pop()


print(stack.displaylist())
