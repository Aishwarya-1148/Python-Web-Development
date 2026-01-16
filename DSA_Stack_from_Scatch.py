class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, data):
        # Use list append method to add element
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

s = Stack()
s.add("Mon")
s.add("Tue")
print("The Peek of Stack is : = ",s.peek())

print("The Peek of Stack is : = ",s.peek())
s.add("Wed")
s.add("Thu")
print("The Peek of Stack is : = ",s.peek())