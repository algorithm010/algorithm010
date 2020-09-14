# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/17 10:38 PM

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        size = len(prices)
        dp = [[0] * 2 for _ in range(size)]
        # 0不持有 1 持有
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])  # hold,sell
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])  # hold,buy,如果i天买入，那么i-2天就不持有
        return dp[-1][0]
        # dp[i][0,1,2,3] 初始状态、买入、卖出、冷冻期
        # dp[i][0] = 0
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0] -p)
        # dp[i][2] = max(dp[i-1][2],dp[i-1][1] + p)
        # dp[i][3] = max(dp[i-1][3],dp[i-1][2])#要么是之前已经闲置，要么是正在闲置-->可以和初始状态合并
        # if not prices: return 0
        # dp = [[0]*3 for _ in range(len(prices))]
        # dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        # for i in range(1,len(prices)):
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][2])
        #     dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
        #     dp[i][2] = max(dp[i-1][2],dp[i-1][1] + prices[i])
        # return dp[-1][2]

        # if not prices: return 0
        # keep, in1, out1 = 0, -prices[0], 0
        # for price in prices:
        #     new_keep = max(keep, out1)
        #     new_in1 = max(in1, keep - price)
        #     new_out1 = max(out1, in1 + price)
        #     keep, in1, out1 = new_keep, new_in1, new_out1
        # return out1

