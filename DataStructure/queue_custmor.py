#write a python programme to create a custmor service by adding the custmor into the queue and once the customer is serve he has to be remove from the queue
class CustomerService:
    def __init__(self):
        self.queue = []
    def add_customer(self, name):
        self.queue.append(name)
        print(f"Customer '{name}' added to the queue.")
    def serve_customer(self):
        if len(self.queue) == 0:
            print("No customers to serve. Queue is empty.")
        else:
            served = self.queue.pop(0)
            print(f"Customer '{served}' has been served and removed from the queue.")
    def display_queue(self):
        if len(self.queue) == 0:
            print("The queue is empty.")
        else:
            print("Current queue:")
            for customer in self.queue:
                print(customer)
service = CustomerService()
service.add_customer("Alice")
service.add_customer("Bob")
service.add_customer("Charlie")
service.display_queue()
service.serve_customer()
service.display_queue()
service.serve_customer()
service.display_queue()

