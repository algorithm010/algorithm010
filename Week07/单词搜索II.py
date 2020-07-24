# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 9:40 PM

# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#  示例:
#
#  输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
#  说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
#  提示:
#
#
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#  Related Topics 字典树 回溯算法
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch,{})
            node['end'] = 0 #将所有word构建为tree树
        rows, cols = len(board), len(board[0])
        res = set()
        def dfs(i,j,root,s):
            cur = board[i][j]
            if cur not in root: return#剪枝
            root = root[cur]#下探
            if 'end' in root and root['end'] == 0:
                res.add(s+cur)#到达叶节点，加入到结果集
            board[i][j] = '@'#
            for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
                tmp_i,tmp_j = x + i, y + j
                if 0 <= tmp_i < rows and 0 <= tmp_j < cols and board[tmp_i][tmp_j]!='@':
                    dfs(tmp_i,tmp_j,root,s + cur)
            board[i][j] = cur#reverse state
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,'')
        return list(res)

