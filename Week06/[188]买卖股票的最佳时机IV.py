# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/17 9:09 PM
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def no_limit(prices):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        size = len(prices)
        if k > size / 2:
            return no_limit(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(size)]
        for i in range(size):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1] + prices[i])#前一天持有并卖掉
                    dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0] - prices[i])#前一天不持有，并买入
        return dp[size - 1][k][0]

        # in_1_k = [float('-inf')] * k
        # in_2_k = [float('-inf')] * k
        # out_1_k = [0] * k
        # out_2_k = [0] * k
        # for j in range(0,k):
        #     for p in prices:
        #         in_1_k[j] = max(in_1_k[j], -p)
        #         out_1_k[j] = max(out_1_k[j], in_1_k[j] + p)
        #         in_2_k[j] = max(in_2_k[j], out_1_k[j] - p)
        #         out_2_k[j] = max(out_2_k[j], in_2_k[j] + p)
        # return out_2_k[k]