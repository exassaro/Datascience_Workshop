class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SCLL:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head  # Pointing to itself (circular)
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            node.next = self.head
            tail.next = node
            self.head = node

    # Insert at the end
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head  # Circular link
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = node
            node.next = self.head  # Circular link to head

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(circular)")

# Example Usage:
scll = SCLL()
scll.insert_beg(10)
scll.insert_end(20)
scll.insert_end(30)
scll.insert_beg(5)
print("Singly Circular Linked List:")
scll.display()
