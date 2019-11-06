

class Node:
    
    def __init__(self, prefix:str, isWord:bool = False):
        self.prefix = prefix
        self.children = {}
        self.isWord = isWord
    
    

from typing import List

class AutoComplete:
    
    def __init__(self, words:List[str]):
        self.root:Node = self.build_trie(words)
        self.result = []
    
    def build_trie(self, words):
        self.root = Node("")
        
        for word in words:
            curr:Node = self.root
            
            for i in range(len(word)):
                prefix = word[0:i+1]
                isWord = i == len(word)-1
                
                if prefix in curr.children:
                    curr = curr.children[prefix]
                    if curr.isWord == False and isWord == True:
                        curr.isWord = True
                else:
                    node= Node(prefix, isWord)
                    curr.children[prefix] = node
                    curr = node
        
        return self.root
    
    
    def find_words(self, prefix:str):
        self.result = []
        curr = self.root
        
        for i in range(len(prefix)):
            if prefix[0:i+1] in curr.children:
                curr = curr.children[prefix[0:i+1]]
            else:
                return None
            
        self.dfs(curr)
        
        return self.result
            
    
    def dfs(self, node:Node):
        
        if node.isWord:
            self.result.append(node.prefix)
        
        for prefix, childNode in node.children.items():
            self.dfs(childNode)
            
                