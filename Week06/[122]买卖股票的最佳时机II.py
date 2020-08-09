# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/16 10:01 PM

from typing import List
class Solution:
    #可以买卖K次
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
        # dp
        # if not prices: return 0
        # dp = [[0] * 2 for _ in range(len(prices))]
        # dp[0][0], dp[0][1] = 0, -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])  # hold,sell
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # hold,buy
        # return dp[-1][0]