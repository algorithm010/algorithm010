# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 8:20 PM

from collections import defaultdict
# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.is_word = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:#Inserts a word into the trie.
#         node = self.root
#         for ch in word:#用word构建Trie树
#             node = node.children[ch]
#         node.is_word = True
#
#     def search(self, word: str) -> bool:#Returns if the word is in the trie.
#         node = self.root
#         for ch in word:
#             if ch in node.children:
#                 node = node.children[ch]
#             else: return False
#         return node.is_word
#
#     def startsWith(self, prefix: str) -> bool:
#         # Returns if there is any word in the trie that starts with the given prefix.
#         node = self.root
#         for ch in prefix:
#             if ch in node.children:
#                 node = node.children[ch]
#             else: return False
#         return True

class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self,word):
        node = self.root
        for ch in word:
            if ch in node:
                node = node.setdefault(ch,{})
        node[self.end_of_word] = self.end_of_word

    def search(self,word):
        node = self.root
        for ch in word:
            if ch in node:
                node = node[ch]
            else: return False
        return self.end_of_word in node

    def startwiths(self,prefix):
        node = self.root
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else: return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)