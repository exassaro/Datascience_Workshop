from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
            return
        self._insert_recur(self.root,val)
        
    def _insert_recur(self,node,val):
        if val < node.value:
            if node.left is None:
                node.left=Node(val)
            else:
                self._insert_recur(node.left,val)
        elif val > node.value:
            if node.right is None:
                node.right=Node(val)
            else:
                self._insert_recur(node.right,val)
                
    def delete(self,key,node):
        if node is None:
            return None
        if key<node.value:
            node.left = self.delete(key, node.left)
        elif key > node.value:
            node.right = self.delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp=self.find_min(node.right)
            node.value=temp.value
            node.right=self.delete(temp.value,node.right)
        return node
    
    def find_min(self,node):
        if node is None:
            return None
        while node.left:
            node=node.left
        return node
    
    
    
    def search(self,key):
        def _search(node,key):
            if node is None:
                return False
            if node.value==key:
                return True
            elif key<node.value:
                return _search(node.left,key)
            else:
                return _search(node.right,key)
        return _search(self.root,key)
    
    def sum_of_nodes(self):
        return self._sum_nodes_rc(self.root)
    
    
    def _sum_nodes_rc(self,node):
        if node is None:
            return 0
        return node.value + self._sum_nodes_rc(node.left) + self._sum_nodes_rc(node.right)
    
    def findclosetnode(self,target):
        return self.findcloset_rc(self.root,target)
    
    def findcloset_rc(self,node,target,closet=None):
        if node is None:
            return closet
        if closet is None or abs(node.value-target)<abs(closet-target):
            closet=node.value
        if target<node.value:
            return self.findcloset_rc(node.left,target,closet)
        else:
            return self.findcloset_rc(node.right, target, closet)
    
        
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
        
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
        
    def preorder(self,node):
        if node is None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    def level_order(self):
        if not self.root:
            return []
        queue=deque([self.root])
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
        return result
    
    def height(self,node):
        if node is None:
            return -1
        return max(self.height(node.left),self.height(node.right)) + 1
    
    def depth(self,root,key,depth=0):
        if root is None:
            return -1
        if root.value==key:
            return depth
        left=self.depth(root.left,key,depth+1)
        if left!=-1:
            return left
        return self.depth(root.right,key,depth+1)
    
    def is_bst(self):
        #check if tree BST using inorder traversal is sorted
        def inorder(node,prev):
            if node is None:
                return True
            if not inorder(node.left,prev):
                return False
            if prev[0] is not None and node.value<=prev[0]:
                return False
            prev[0]=node.value
            return inorder(node.right,prev)
        return inorder(self.root,[None])
    
    
tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(0)
tree.insert(100)

print("\nBefore Deleting 10:")
print("Inorder Traversal:", end=" ")
tree.inorder(tree.root)  # Should print 0 10 20 100
print("\nIs the tree a BST?", tree.is_bst())  # ✅ True

tree.delete(10, tree.root)  # Delete 10

print("\nAfter Deleting 10:")
print("Inorder Traversal:", end=" ")
tree.inorder(tree.root)  # Should print 0 20 100
print("\nIs the tree a BST?", tree.is_bst())  # ✅ True

print("\nSearch 20:", tree.search(20))  # ✅ True
print("Sum of nodes:", tree.sum_of_nodes())  # ✅ 120
print("Closest to 20:", tree.findclosetnode(20))  # ✅ 20
print("Depth of 100:", tree.depth(tree.root, 100))  # ✅ Should return depth level
print("Height of tree:", tree.height(tree.root))  # ✅ Should return tree height
print("\nLevel Order Traversal:", tree.level_order())  