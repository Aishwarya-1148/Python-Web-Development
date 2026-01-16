# QUEUE IMPLEMENTATION USING DEQUE : Definition
# A Queue is a linear data structure that follows the principle: FIFO – First In, First Out
# This means:The first element added is the first one removed

"""
3️⃣ Queue (FIFO)
    Where it is used:
    When tasks must be processed in the order they arrive
Real Project Examples:
    Printer job scheduling
    Customer support ticket system
    Request handling in web servers
    Task scheduling in operating systems
Why queue is used:
    Maintains fairness
    Order-based processing
    Prevents starvation
"""

# We are importing collection Because Python list is NOT efficient for queue operations.
"""
What is collections in Python?
collections is a built-in Python module
It provides specialized container datatypes (data structures) that are more powerful than 
basic lists, tuples, or dictionaries. Examples of what collections provides:
deque → Double-ended queue
"""
from collections import deque # 
queue = deque()

queue.append(10)# Enqueue : Insert Operation is called as Enqueue
queue.append(20)
queue.append(30)
print("Queue after enqueue:", queue)

# Dequeue : Delete Operation is called as Dequeue
print("Dequeued element:", queue.popleft()) # It removes and returns the element from the left end (front) of the deque

print("Front element:", queue[0])# Front element 

if not queue:# Check empty : Checking Whether the Queue is empty or not 
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Final queue:", queue)



