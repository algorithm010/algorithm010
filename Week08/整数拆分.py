# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/30 7:58 PM

from functools import lru_cache
class Solution:
    @lru_cache
    def integerBreak(self, n: int) -> int:
        # 怎么感觉又是零钱兑换、背包问题
        res = 0
        for i in range(1, n-1):
            res = max(res, (n-i)*i, i * self.integerBreak(n-i))
        return res
        # f(n) = f(n-1,1) f(n-2,2) f(n-3,3)
        # dp = [1] * (n + 1)
        # for i in range(3, n + 1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], max(dp[j], j) * (i - j))
        # return dp[-1]



s = Solution()
res = s.integerBreak(10)
print(res)