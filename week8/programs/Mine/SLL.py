class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Creating Singly Linked List
class Sll:
    def __init__(self):
        self.head = None
        
    # Insert at end
    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    
    # Insert at beginning
    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node
    
    # Insert before an element
    def insert_bef(self, target, data):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == target:
            self.insert_beg(data)
            return
        curr = self.head
        while curr.next and curr.next.data != target:
            curr = curr.next
        if curr.next is None:
            print(f"Element {target} not found")
            return
        node = Node(data, curr.next)
        curr.next = node
    
    # Insert after an element
    def insert_aft(self, target, data):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr is None:
            print(f"Element {target} not found")
            return
        node = Node(data, curr.next)
        curr.next = node
    
    # Insert array
    def insert_arr(self, arr):
        for data in arr:
            self.insert_end(data)
    
    # Insert at specific position
    def insert_pos(self, pos, data):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_beg(data)
            return
        curr = self.head
        count = 1
        while curr and count < pos - 1:
            curr = curr.next
            count += 1
        if curr is None:
            print("Position out of range")
            return
        node = Node(data, curr.next)
        curr.next = node
    
    # Delete beginning
    def delete_beg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
    
    # Delete end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
    
    # Delete specific element
    def delete_elmnt(self, target):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != target:
            curr = curr.next
        if curr.next is None:
            print(f"Element {target} not found")
            return
        curr.next = curr.next.next
    
    # Delete at specific position
    def delete_pos(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position")
            return
        if pos == 1:
            self.head = self.head.next
            return
        curr = self.head
        count = 1
        while curr.next and count < pos - 1:
            curr = curr.next
            count += 1
        if curr.next is None:
            print("Position out of range")
            return
        curr.next = curr.next.next
    
    # Search element
    def search(self, target):
        curr = self.head
        pos = 1
        while curr:
            if curr.data == target:
                return pos
            curr = curr.next
            pos += 1
        return "Element not found"
    
    # Find element at position
    def find_pos(self, pos):
        curr = self.head
        count = 1
        while curr:
            if count == pos:
                return curr.data
            curr = curr.next
            count += 1
        return "Position out of range"
    
    # Find middle
    def find_mid(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
        
    # Delete middle element
    def delete_mid(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = slow.next
            
    
        
    # Remove adjacent duplicates
    def rmv_adjdup(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
    
    # Remove duplicates
    def rmv_dup(self):
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next
            
    # Reverse list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        
    # Sort list
    def sort(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            next_node = curr.next
            while next_node:
                if curr.data > next_node.data:
                    curr.data, next_node.data = next_node.data, curr.data
                next_node = next_node.next
            curr = curr.next
            
    # Split list
    def split(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        first_half = Sll()
        second_half = Sll()
        first_half.head = self.head
        second_half.head = slow
        prev.next = None
        return first_half, second_half
    
    # Convert to circular linked list
    def to_circular(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = self.head
    
    #Detect cycle    
    def detect_cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
            
        
    
    # Find length
    def length(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count
    
    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


sll = Sll()
sll.insert_beg(10)
sll.insert_beg(22)
sll.insert_end(45)
sll.insert_aft(10, 15)
sll.insert_bef(22, 12)
sll.insert_pos(5, 86)
print("Insertion operations:")
sll.display()
sll.delete_pos(2)
sll.delete_beg()
sll.delete_end()
sll.delete_elmnt(15)
print("Deletion operations:")
sll.display()
x = [3, 4, 5, 87, 65, 21, 34]
sll.insert_arr(x)
print("Array inserted:")
sll.display()
print("Element at position 4:", sll.find_pos(4))
print("Position of element 65:", sll.search(65))
print("Middle element:", sll.find_mid())
sll.delete_mid()
print("Delete middle: ")
sll.display()
x = [12,12, 5, 34, 65, 21, 34]
sll.insert_arr(x)
print("Array inserted:")
sll.display()
sll.rmv_adjdup()
print("adjacent duplicate removed: ")
sll.display()
sll.rmv_dup()
print("duplicates removed:")
sll.display()
sll.reverse()
print("Reversed list:")
sll.display()
print("Length of list:", sll.length())
sll.sort()
print("Sorted list:")
sll.display()
print("Split to two:")
first_half, second_half = sll.split()

print("First Half:")
first_half.display()

print("Second Half:")
second_half.display()

print("detect cycle: ")
print(sll.detect_cycle())
print("convert to circular")
sll.to_circular()
print("detect cycle: ")
print(sll.detect_cycle())


