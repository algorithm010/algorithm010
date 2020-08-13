# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/21 9:15 PM

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 皇后放置问题，八个数的全排列N! 所以时间复杂度就是N!,空间复杂度O(N)
        # record记录皇后的放置情况
        def dfs(row,record):
            if row == n:
                res.append(record)
                return
            for col in range(n):
                if isvalid(row,col,record):
                    dfs(row+1,record+[col])
        def isvalid(row,col,record):
            if col in record:#这一行肯定不能被其他皇后占据
                return False
            for i in range(row):#判断是否在可攻击范围
                # if row + col == i + record[i] or row - col == i - record[i]:
                if i + record[i] == row + col or i - record[i] == row - col:
                    return False
            return True
        res = []
        dfs(0,[])
        return [['.' * i + 'Q' +'.'*(n-i-1) for i in row]for row in res]