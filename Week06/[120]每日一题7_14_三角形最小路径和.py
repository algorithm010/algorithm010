# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/14 12:43 AM

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1.分治 F[i,j] = min(F[i+1,j],f[i,j+1]) + a[i,j]
        # from functools import lru_cache
        # @lru_cache(None)
        # def dfs(row,col):
        #     if row == size - 1:return triangle[row][col]
        #     left = dfs(row+1,col)
        #     right = dfs(row+1,col+1)
        #     return min(left,right) + triangle[row][col]
        # size = len(triangle)
        # return dfs(0,0)

        # res = triangle[-1]
        # for i in xrange(len(triangle)-2, -1, -1):
        #     for j in xrange(len(triangle[i])):
        #         res[j] = min(res[j], res[j+1]) + triangle[i][j]
        # return res[0]
        # dp = triangle
        # for i in range(len(dp)-2,-1,-1):
        #     for j in range(len(dp[i])):
        #         dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + dp[i][j]
        # return dp[0][0]
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


nums = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
res = s.minimumTotal(nums)
print(res)
