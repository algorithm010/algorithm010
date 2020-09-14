# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/1 11:47 PM

from typing import List


class Solution:

    def generate(self, rows: int) -> List[List[int]]:
        # dp = [[0]* rows for _ in range(rows)]
        # for row in range(rows):
        #     dp[row][0] = 1
        # for i in range(1,rows):
        #     for j in range(rows):
        #         if i-1 >= 0:
        #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #
        # for i in range(rows):
        #      #第0行pop四个，第1行pop3个、2 2 、3 1 4，0
        #      tmp = rows-i-1
        #      for i in range(tmp):
        #          dp[i].pop()
        # return dp
        #这里只用返回第k行  想办法优化到O(K)，每次在dp上覆盖修改
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        # [1, 5, 10, 10, 5, 1]
        # dp = [0] * (rows+1)
        # dp[0] = 1
        # print(dp)
        # for i in range(1, rows+1):
        #     for j in range(1, i):#2
        #         dp[j] = dp[j]+dp[j-1]#
        #     print(dp)
        #     dp[i] = 1
        # return dp
        dp = [1] * (rows + 1)
        for i in range(2, rows + 1):
            for j in range(i - 1, 0, -1):#首尾的1，不用更新
                dp[j] += dp[j - 1]
        return dp
        # dp =[1]
        # for i in range(1, rows + 1):
        #     dp.append(0)
        #     for j in range(1, i + 1):
        #         dp[-j] = dp[-j] + dp[-j - 1]
        # print(dp)
        # return dp

s = Solution()
res = s.generate(3)
# print(res)