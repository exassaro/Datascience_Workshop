class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None
        
        
class Tree:
    def __init__(self):
        self.root=None
        
    #insert value in tree    
    def insert(self,val):
        if not self.root:
            self.root=Node(val)
            return
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            if curr.left is None:
                curr.left=Node(val)
                return
            else:
                queue.append(curr.left)
            if curr.right is None:
                curr.right=Node(val)
                return
            else:
                queue.append(curr.right)
                
                
    #delete value in tree           
    def delete(self,val):
        if not self.root:
            return None
        node_delete=None
        queue=[self.root]
        last_node=None
        last_parent=None
        
        while queue:
            curr=queue.pop(0)
            
            if curr.value==val:
                node_delete=curr
            
            if curr.left:
                last_parent=curr
                queue.append(curr.left)
            if curr.right:
                last_parent=curr
                queue.append(curr.right)
                
            last_node = curr
            
        if not node_delete:
            return False
        
        node_delete.value=last_node.value
        
        queue=[self.root]
        
        if last_parent:
            if last_parent.left==last_node:
                last_parent.left=None
            elif last_parent.right==last_node:
                last_parent.right=None
        else:
            self.root=None
            
        return True

                
    #Search a value
    def search(self,val):
        if not self.root:
            return False
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            if curr.value==val:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False
    
    #find depth of tree
    def find_depth(self,root,key,depth=0):
        if root is None:
            return -1
        if root.value==key:
            return depth
        left_depth=self.find_depth(root.left,key,depth + 1)
        if left_depth != -1:
            return left_depth
        return self.find_depth(root.right,key,depth+1)
    
    #find height of tree
    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        return max(left_height,right_height)+1
    
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value,end=" ")
        self.inorder(node.right)
        
    def preorder(self,node):
        if node is None:
            return
        print(node.value,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value,end=" ")
        
    def level_order(self):
        if not self.root:
            return None
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            print(curr.value,end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        
        
    def find_min(self):
        if not self.root:
            return None
        queue=[self.root]
        min_value=float("inf")
        while queue:
            curr = queue.pop(0)
            min_value=min(min_value,curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return min_value
    
    def find_max(self):
        if not self.root:
            return None
        queue=[self.root]
        max_value=float("-inf")
        while queue:
            curr = queue.pop(0)
            max_value=max(max_value,curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return max_value
    
    
bt = Tree()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)
bt.insert(60)
bt.insert(70)

print("Inorder Traversal: ", end="")
bt.inorder(bt.root)
print("\nPreorder Traversal: ", end="")
bt.preorder(bt.root)
print("\nPostorder Traversal: ", end="")
bt.postorder(bt.root)
print("\nLevel Order Traversal: ", end="")
bt.level_order()

print("\nMin Value:", bt.find_min())
print("Max Value:", bt.find_max())

print("Depth of node 50:", bt.find_depth(bt.root, 50))
print("Height of tree:", bt.height(bt.root))

bt.delete(40)
print("\nAfter Deletion (Inorder Traversal): ", end="")
bt.inorder(bt.root)
