class Queue:
    def __init__(self):
        self.items = []
    #Add item to rear(end)
    def enqueue(self,item):
        self.item.append(item)
    #check Queue is Empty or not
    def is_empty(self):
        return len(self.items) == 0
    #Remove and return front item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    #look at front item without removing
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
     #look at rear item without removing
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def size(self):
        return len(self.items)