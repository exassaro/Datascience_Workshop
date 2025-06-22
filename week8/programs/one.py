# DOUBLE LinkedList(allow traversal at both forward and backward direction)
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def _init_(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("LL is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end="<-->")
            temp = temp.next
        print("none")

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def afternode(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        new_node = Node(data)
        current = self.head
        while current is not None:
            if current.data == x:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
            current = current.next

    def beforenode(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                current.next.prev = new_node
                return
            current = current.next

    def delebegin(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head is not None:
            self.head = self.head.next
            self.head.next.prev = None
            return
        self.head = None  # if only one node

    def delelast(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delespeci(self, x):
        if self.head is None:
            print("LL is emoty")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.next.prev = None
            return
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                return
            current = current.next

    def middledele(self):
        fast = self.head
        slow = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next


DLL1 = DLinkedList()
DLL1.append(10)
DLL1.append(14)
DLL1.append(16)
DLL1.begin(9)
DLL1.afternode(12, 10)
DLL1.beforenode(11, 12)
DLL1.delebegin()
DLL1.delelast()
DLL1.delespeci(9)
DLL1.middledele()
DLL1.display()