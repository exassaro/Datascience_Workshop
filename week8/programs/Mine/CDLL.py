class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            tail.next = node
            self.head.prev = node
            self.head = node

    # Insert at the end
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = node
            node.prev = tail
            node.next = self.head
            self.head.prev = node

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" <--> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(circular)")

# Example Usage:
dcll = DCLL()
dcll.insert_beg(10)
dcll.insert_end(20)
dcll.insert_end(30)
dcll.insert_beg(5)
print("Doubly Circular Linked List:")
dcll.display()
