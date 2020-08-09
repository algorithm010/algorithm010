# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/5 9:11 PM


from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        #进行初始化
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1,len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
        # dp = [0] * (amount+1)
        # dp[0] = 1
        # for coin in coins:#[1,2,5]
        #     for i in range(coin,amount+1):
        #         dp[i] += dp[i-coin]
        # return dp[-1]

s = Solution()
coins = [1,101,102,103]
res = s.change(100,coins)
print(res)
