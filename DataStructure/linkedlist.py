class node:
    def __init__(self,data):
        self.data = data
        self.next = None
Frist = node(10)
Second = node(20)
Third = node(30)
Fourth = node(40)
Fifth = node(50)
head = Frist
Frist.next = Second
Second.next = Third
Third.next = Fourth
Fourth.next = Fifth
current = head
while current:
    print(current.data,end="--->")
    current = current.next
print("None")
#write a python programme to create a linkedlist of size n take the ā value of n as input from the user
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n = int(input("Enter size of linked list: "))
val = int(input("Enter value for node 1: "))
head = Node(val)
temp = head
for i in range(2, n+1):
    val = int(input(f"Enter value for node {i}: "))
    temp.next = Node(val)
    temp = temp.next
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
