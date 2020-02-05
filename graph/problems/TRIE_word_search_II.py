'''
212. Word Search II
Hard

1756

89

Add to List

Share
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''

from typing import List
from collections import defaultdict


class TrieNode:
    
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    
    




class Solution:

    def __init__(self):
        self.root = TrieNode()


    def add_word_to_trie(self, word: str):
        cur = self.root

        for i in range(0, len(word)):
            cur = cur.children[word[i]]

            if i == len(word) -1:
                cur.is_word = True


    def findWords(self, board: List[List[str]], words: List[str]):
        
        for word in words:
            self.add_word_to_trie(word)

        self.res = []
        
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                self.dfs(board, row, col, self.root, '', set())

        return self.res


    
    def dfs(self, board, row, col, node, prefix, visited):
    
        if not node:
            return

        visited.add(f'{row} {col}')

        if board[row][col] in node.children:
            prefix += board[row][col]
            node = node.children[board[row][col]]

            if node.is_word:
                self.res.append(prefix)
                node.is_word = False

            adj_offsets = [(0,1), (0,-1), (1,0), (-1,0)]

            for ro, co in adj_offsets:
                adj_row = row + ro
                adj_col = col + co

                if adj_row >= 0 and adj_row < len(board) and adj_col >= 0 and adj_col < len(board[adj_row]) and f'{adj_row} {adj_col}' not in visited:
                        self.dfs(board, adj_row, adj_col, node, prefix, visited)        

        



                
    
    



board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]

sol = Solution()
print(sol.findWords(board, words))
