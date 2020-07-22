# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/21 9:15 PM

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row, record):
            if row == n:
                res.append(record)
                return
            for col in range(n):
                if isvalid(row, col, record):#判断这一行的这一列 是否合法
                    dfs(row+1, record+[col])#record下标为行值为列
        def isvalid(row,col, record):
            if col in record: return False
            for i in range(row):
                if row + col == i + record[i] or row - col == i - record[i]:
                    return False
            return True
        res = []
        dfs(0,[])
        # print(res)
        return [['.' * i + 'Q' + '.'* (n-i-1) for i in row] for row in res]