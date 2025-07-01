from collections import deque
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing:", queue)
first = queue.popleft()
print("Dequeue element:",first)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front element:",queue[0])

#stack
from collections import deque 
stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing:", stack)
top =  stack.pop()
print("Popped element:", top)
print("Stack after popping:", stack)
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
print("Front element:", stack[0])
    