class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self):
        self.head = None

    # Convert to circular doubly linked list
    def convert_to_circular(self):
        if self.head is None:
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = self.head  # Connect last node to head
        self.head.prev = last  # Connect head to last node

    # Insert at the end (maintains circular property)
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
            return
        last = self.head.prev  # Get the last node
        last.next = node
        node.prev = last
        node.next = self.head  # Connect new node to head
        self.head.prev = node  # Update head's previous pointer

    # Insert at the beginning (maintains circular property)
    def insert_beg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
            return
        last = self.head.prev  # Get the last node
        node.next = self.head
        self.head.prev = node
        last.next = node
        node.prev = last
        self.head = node  # Update head to new node

    # Display circular DLL
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <--> ")
            temp = temp.next
            if temp == self.head:  # Stop when loop completes
                break
        print("(circular)")

# Example usage
dll = Dll()
dll.insert_beg(10)
dll.insert_beg(22)
dll.insert_end(45)
dll.insert_end(15)

print("Before conversion to circular:")
dll.display()

dll.convert_to_circular()

print("After conversion to circular:")
dll.display()
