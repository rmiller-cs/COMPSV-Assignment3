from node import Node

# stack class for undo/redo
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty.")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()
            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.peek()
            if action == None:
                print("No action to undo.")
            else:
                undo_stack.pop()
                redo_stack.push(action)
            
        elif choice == "3":
            action = redo_stack.peek()
            if action == None:
                print("No action to redo.")
            else:
                redo_stack.pop()
                undo_stack.push(action)

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()