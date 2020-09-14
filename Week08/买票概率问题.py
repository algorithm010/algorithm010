# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/1 9:39 PM

from functools import lru_cache
class Solution:
    # @lru_cache
    def buy_tickets(self, m, n):# m,n 分别代表50，100
        # 假设第m+n个人手持100,则他前面有m个手持50，n-1个手持100 则f(m,n) = f(m,n-1)
        # m+n手持50.他前面m-1个手持50，n个手持100 f(m,n) = f(m-1,n)
        # m<n -> 0; n=0 -> 1
        res = 0
        if n == 0:
            return 1
        elif m < n:
            return 0
        else:
            res = self.buy_tickets(m,n-1) + self.buy_tickets(m-1,n)
        return res
    def buy_ticketsI(self,m,n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        for col in range(n+1):
            dp[0][col] = 0
        for row in range(m+1):
            dp[row][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i < j: dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


s = Solution()
res = s.buy_ticketsI(20,10)
print(res)
