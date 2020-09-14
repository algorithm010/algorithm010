# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/21 9:15 PM

from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        #预先扫描一次
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cols[i].add(board[i][j])
                    rows[i].add(board[i][j])
                    boxs[i//3*3+j//3].add(board[i][j])

        def dfs(i, j):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    self.flag = True
                    return
                if j < 8:
                    dfs(i, j + 1)
                else:
                    dfs(i + 1, 0)
                return
            for ch in range(1, 10):#对于每一个位置，用1-9试探
                ch = str(ch)
                if ch not in cols[j] and ch not in rows[i] and ch not in boxs[i // 3 * 3 + j // 3]:
                    #如果可以放置，更新三个set()，并将此刻的位置修改
                    cols[j].add(ch)
                    rows[i].add(ch)
                    boxs[i // 3][j // 3].add(ch)
                    board[i][j] = ch
                    if i == 8 and j == 8:
                        self.flag = True
                        return
                    if j < 8:
                        dfs(i, j + 1)
                    else:
                        dfs(i + 1, 0)
                    if self.flag: return
                    board[i][j] = '.'
                    cols[j].remove(ch)
                    rows[i].remove(ch)
                    boxs[i // 3][j // 3].remove(ch)

        self.flag = False
        dfs(0, 0)
