
class Node:
    def __init__(self):
        self.child=[None]*26
        self.end=False
        self.count=0
        
class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self,key):
        curr=self.root
        for i in key:
            index=ord(i)-ord('a')
            if not curr.child[index]:
                curr.child[index]=Node()
            curr=curr.child[index]
            curr.count+=1
        curr.end=True
        
    def display(self):
        def dsp(curr,word):
            if curr.end:
                print(word)
            for i in range(26):
                if curr.child[i]:
                    dsp(curr.child[i],word + chr(i+ord('a')))
        dsp(self.root,'')
    
    def search(self,key):
        curr=self.root
        for i in key:
            index=ord(i)-ord('a')
            if not curr.child[index]:
                return False
            curr=curr.child[index]
        return curr.end
    
    def prefixsearch(self,key):
        curr=self.root
        for i in key:
            index=ord(i)-ord('a')
            if not curr.child[index]:
                return False
            curr=curr.child[index]
        return True
    
    def delete_key(self,key):
        def _delete(curr,key,depth):
            if curr is None:
                return False
            if depth==len(key):
                if curr.end:
                    curr.end=False
                    return not any(curr.child)
                return False
            index=ord(key[depth])-ord('a')
            should_delete_curr=_delete(curr.child[index],key,depth+1)
            if should_delete_curr:
                curr.child[index]=None
                return not curr.end and not any(curr.child)
            return False
        return _delete(self.root,key,0)
    
    def autocomplete(self,prefix):
        curr=self.root
        for char in prefix:
            index=ord(char)-ord('a')
            if not curr.child[index]:
                return []
            curr=curr.child[index]
        result=[]
        self._collect_words(curr,prefix,result)
        return result
    
    def _collect_words(self,node,word,result):
        if node.end:
            result.append(word)
        for i in range(26):
            if node.child[i]:
                self._collect_words(node.child[i],word+chr(i+ord('a')),result)
                
    def longest_prefix(self):
        curr = self.root
        prefix = ""
        while curr:
            children = [i for i in range(26) if curr.child[i] is not None]
            if len(children) == 1 and not curr.end:  # Stop if branching occurs or end of a word is reached
                index = children[0]
                prefix += chr(index + ord('a'))
                curr = curr.child[index]
            else:
                break
        return prefix


    
    def count_words_with_prefix(self,prefix):
        curr=self.root
        for char in prefix:
            index=ord(char)-ord('a')
            if not curr.child[index]:
                return 0
            curr=curr.child[index]
        return curr.count
    
    def find_unique_prefix(self, key):
        curr = self.root
        prefix = ""
        for char in key:
            index = ord(char) - ord('a')
            if not curr.child[index]:  # Check if the node exists
                return prefix
            if curr.child[index].count == 1:
                prefix += char
                return prefix
            prefix += char
            curr = curr.child[index]
        return prefix

        
ob = Trie()
ob.insert('abcd')
ob.insert('abcde')
ob.insert('abc')

ob.display()
print("Longest Prefix:", ob.longest_prefix())  # Should return 'abc' because 'abcd', 'abcde', 'abc' share it
ob.insert('how')
ob.insert('home')
print("Count Words with Prefix 'ho':", ob.count_words_with_prefix('ho'))  # Should return 2 ('how', 'home')
print("Unique Prefix of 'home':", ob.find_unique_prefix('home'))  # Should return 'hom'                
                
                