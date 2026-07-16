# Stack using Linked List with User Input

class Node:
    def __init__(self, title):
        self.title = title
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, title):
        new_node = Node(title)
        new_node.next = self.top
        self.top = new_node
        print("Book added successfully!")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty. No book to retrieve.")
        else:
            print("Retrieved Book:", self.top.title)
            self.top = self.top.next

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("\nBooks in Stack (Top to Bottom):")
            temp = self.top
            while temp:
                print(temp.title)
                temp = temp.next

# Main Program
stack = Stack()

while True:
    print("\n----- Library Stack Menu -----")
    print("1. Push Book Title")
    print("2. Pop Book Title")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter Book Title: ")
        stack.push(title)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
