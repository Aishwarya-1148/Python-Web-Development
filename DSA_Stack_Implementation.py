# STACK IMPLEMENTATION USING LIST : A Stack is a linear data structure that follows the principle:
# LIFO – Last In, First Out

"""
2️⃣ Stack (LIFO)
    Where it is used:
    When the last action must be processed first
Real Project Examples:
    Undo / Redo operations in editors
    Browser back and forward buttons
    Function call handling (call stack)
    Expression evaluation in compilers
Why stack is used:
    Simple push and pop operations
    Manages nested operations efficiently
"""

stack = [] # creating an empty stack 

# Push operation (insert operation  )
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop operation ( Delete Operation )
print("Popped element:", stack.pop())

# Peek operation (stack top element )
print("Top element:", stack[-1])

# Check empty : checking whether the stack is empty or not 
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
print("Final stack:", stack) # printing the stack with all the element present in the stack 

