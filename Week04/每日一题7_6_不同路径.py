# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/6 6:57 PM
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #排列组合Cm-1,m+n-2
        # return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))
        #动态规划
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m - 1][n - 1]

m, n = 3, 7
s = Solution()
res = s.uniquePaths(m,n)
print(res)
