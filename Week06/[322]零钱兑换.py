# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/15 12:38 AM

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @functools.lru_cache(amount)
        # def dfs(coins,amount,i,count,res):
        #     if amount == 0: return min(count,res)
        #     if i == -1: return res#coins下标为0还没有使得amount=0，那么找不到了
        #     m = amount//coins[i]
        #     while m >= 0 and m+count < res:
        #         res = dfs(coins,amount-m*coins[i],i-1,m+count,res)
        #         m = m - 1
        #     return res
        # coins.sort()
        # res = dfs(coins,amount,len(coins)-1,0,float('inf'))
        # return res if res!=float('inf') else -1
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        #dp[i]代表拼凑出i元的最少纸币数
        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i-coin] + 1,dp[i])
        return dp[-1] if dp[-1]!=float('inf') else -1
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0
        # for i in range(amount + 1):
        #     for coin in coins:
        #         if i >= coin:  # 实际上是min(dp[i-coin1]+1,dp[i-coin2]+1,dp[i-coin3]+1)
        #             dp[i] = min(dp[i - coin] + 1, dp[i])
        # return dp[-1] if dp[-1] != float('inf') else -1


