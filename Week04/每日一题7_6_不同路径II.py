# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/6 7:36 PM
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or len(obstacleGrid)==0: return 0
        m, n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i]==0:
                dp[0][i] = 1
        for j in range(m):
            if obstacleGrid[j][0]==0:
                dp[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m - 1][n - 1]

nums = [
  [0,0,0,0,0,0],
  [0,1,0,0,0,0],
  [0,0,0,0,0,0]
]
nums1 = [[1,0]]
s =Solution()
res = s.uniquePathsWithObstacles(nums1)
print(res)