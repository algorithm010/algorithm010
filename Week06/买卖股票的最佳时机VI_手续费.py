# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/17 11:33 PM

from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0],dp[i][1] 买入的最大值，卖出的最大值
        # dp = [[0, 0] for _ in range(len(prices))]
        # dp[0][0], dp[0][1] = -prices[0] - fee, 0
        # # 每笔交易你只需要为支付一次手续费, 可以在买入的时候付，也可以在卖出的时候付，这里在买入的时候付
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] - fee)  # 持股
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 不持股
        # return dp[-1][1]
        #降维
        in1, out1 = -prices[0] - fee, 0
        for price in prices:
            in1 = max(in1, out1-price-fee)
            out1 = max(out1, in1 + price)
        return out1




s = Solution()
res = s.maxProfit(prices = [1, 3, 2, 8, 4, 9],fee=2)
print(res)