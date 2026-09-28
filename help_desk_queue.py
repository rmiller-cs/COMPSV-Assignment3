from node import Node

# queue class for help desk
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None

    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next
    

def run_help_desk():
    support_queue = Queue()
    
    
    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            support_queue.enqueue(name)
            print(f"{name} was added to the queue.")

        elif choice == "2":
            name = support_queue.peek()
            support_queue.dequeue()
            print(f"{name} had their request handled.")

        elif choice == "3":
            name = support_queue.peek()
            print(f"{name} is the next person in queue.")

        elif choice == "4":
            print("\nWaiting customers:")
            support_queue.print_queue()
            
        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
