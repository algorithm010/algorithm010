# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/1 9:26 PM

from typing import List
class Solution:
    '''
    将二维网格视作一个无向图，竖直或水平相邻的'1'右边
    遍历这个二维网格，如果某点='1'，则以该点做深度优先搜索
    在深度优先搜索过程中，将已经访问过的节点标记为'0' 最后的岛屿数量就是待求值
    深度优先过程中，我们考察该点十字型结构有没有等于1的，进而深度遍历
    时间复杂度是O(MN)，最坏情况下的空间复杂度为O(MN)，此时整个二维网格全为1
    '''
    #深度优先搜索
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1
        return islands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
    #广度优先搜索
    # 维护一个队列，做广度优先搜索，搜索其十字型中是否为'1'，是则加入队列中
    # 最后返回的结果就是我们广度搜索的次数
    def numIslandsI(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])
        count = 0
        quene = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count = count + 1
                    quene.append((i, j))
                    while quene:
                        row, col = quene.pop()
                        if col + 1 < cols and grid[row][col + 1] == '1':
                            quene.append((row, col + 1))
                            grid[row][col + 1] = 0
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            quene.append((row, col - 1))
                            grid[row][col - 1] = 0
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            quene.append((row - 1, col))
                            grid[row - 1][col] = 0
                        if row + 1 < rows and grid[row + 1][col] == '1':
                            quene.append((row + 1, col))
                            grid[row + 1][col] = 0
        return count

