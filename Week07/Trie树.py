# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 8:20 PM


# 节点不存完整单词
# 从根节点到某一节点，路径上的字符连接起来为该节点的字符串
# 每个节点的所有子节点路径代表不同的字符串
# 需要实现三个方法1.insert、search、startwith
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)