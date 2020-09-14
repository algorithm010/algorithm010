# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/24 10:17 PM


# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
#  示例:
#
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
#  提示：
#
#
#  board 和 word 中只包含大写和小写英文字母。
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#  1 <= word.length <= 10^3
#
#  Related Topics 数组 回溯算法

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, board, word):
                    return True
        return False

    def dfs(self, i, j, board, word):
        if len(word) == 0: return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return  # 回溯
        tmp = board[i][j]
        board[i][j] = '#'  # 标志着已经选用过,到下一层哪怕选了 也是!=word[0],会回溯
        res = self.dfs(i + 1, j, board, word[1:]) or self.dfs(i - 1, j, board, word[1:]) \
              or self.dfs(i, j + 1, board,word[1:]) or self.dfs(i,j - 1,board,word[1:])
        board[i][j] = tmp
        return res

