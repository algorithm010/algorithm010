# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/17 1:36 AM

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        #0未买入 1 买入一次 2 卖出一次 3 买入两次 4 卖出2次
        # dp = [[0]*len(prices) for _ in range(2*2+1)]
        dp = [[0]*5 for _ in range(len(prices))]
        dp[0][0] = dp[0][2] = dp[0][4] = 0
        dp[0][1] = dp[0][3] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = 0 #如果第i天没有买入，那么只可能i-1天没有买入
            #第i天买入一次，可能是i-1天未买i天买 或 第i-1天买i未买
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            #第i天买入一次卖出一次，可能是i-1天买入i天卖出或者i-1天已经买入卖出了
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            #第i天买入2次卖出1次，可能是i-1买卖(1,1)次，i天买入；也可能是是i-1天已经买卖(2,1)次
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            # 第i天买卖(2,2)可能是i-1天买卖(2,2)也可能是i-1天买卖(2,1)，i卖出
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        #最后手头没有股票剩余，实际收益最高
        return dp[-1][4]


        # if not prices: return 0
        #0未买入 1 买入一次 2 卖出一次 3 买入两次 4 卖出2次
        # dp = [[0]*len(prices) for _ in range(2*2+1)]
        # dp = [[0]*5 for _ in range(len(prices))]
        # dp[0][0] = dp[0][2] = dp[0][4] = 0
        # dp[0][1] = dp[0][3] = -prices[0]
        # for i in range(1,len(prices)):
        #     dp[i][0] = 0 #如果第i天没有买入，那么只可能i-1天没有买入
        #     #第i天买入一次，可能是i-1天未买i天买 或 第i-1天已买
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        #     #第i天买入一次卖出一次，可能是i-1天买入i天卖出或者i-1天已经买入卖出了
        #     dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
        #     #第i天买入2次卖出1次，可能是i-1买卖(1,1)次，i天买入；也可能是是i-1天已经买卖(2,1)次
        #     dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
        #     # 第i天买卖(2,2)可能是i-1天买卖(2,2)也可能是i-1天买卖(2,1)，i卖出
        #     dp[i][4] = max(dp[i-1][4], dp[i-1][3]) + prices[i] #这一行写错了
        # #最后手头没有股票剩余，实际收益最高
        # return max(dp[-1][2],dp[-1][4])

        # one_buy = two_buy = float('inf')
        # one_profit = two_profit = 0
        # for p in prices:
        #     one_buy = min(one_buy, p)
        #     one_profit = max(one_profit, p - one_buy)
        #     two_buy = min(two_buy, p - one_profit)
        #     two_profit = max(two_profit, p - two_buy)
        # return two_profit

s = Solution()
nums = [3,3,5,0,0,3,1,4]
res = s.maxProfit(nums)
print(res)