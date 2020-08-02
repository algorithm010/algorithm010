# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/1 11:30 PM

from typing import List


class Solution:

    def generate(self, rows: int) -> List[List[int]]:
        dp = [[0]* rows for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = 1
        for i in range(1,rows):
            for j in range(rows):
                if i-1 >= 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        for i in range(rows):
             #第0行pop四个，第1行pop3个、2 2 、3 1 4，0
             tmp = rows-i-1
             for i in range(tmp):
                 dp[i].pop()
        return dp

s = Solution()
res = s.generate(5)
print(res,'\n')