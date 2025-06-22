class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
        
root=Node(10)
root.left=Node(20)
root.right=Node(12)

print(root.left.val)