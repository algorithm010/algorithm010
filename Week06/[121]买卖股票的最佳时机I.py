# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/16 9:06 PM

from typing import List
class Solution:
    # 只能买卖一次
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力法 O(N^2)枚举第i天买入第j天卖出，记录最大值
        # res = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         res = max(res,prices[j]-prices[i])
        # return res
        # 动态规划 到第i天获得的最大收益等于到第i-1天的最大收益 和 当前股价与当前最低股价差值之间的最大值

        # if not prices: return 0
        # dp = [0] * len(prices)
        # lowest = prices[0]
        # for i in range(1, len(prices)):
        #     if prices[i] < lowest:
        #         lowest = prices[i]
        #     dp[i] = max(dp[i - 1], prices[i] - lowest)#状态转移只与前一个状态有关
        # return dp[-1]
        if not prices: return 0
        pre, cur, lowest = 0,0,prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
              lowest = prices[i]
            # cur = max(cur,prices[i]-lowest)
            pre, cur = cur, max(cur, prices[i]-lowest)
            print(pre,cur)
        # return max(cur,pre)
        return cur



s = Solution()
res = s.maxProfit([7,1,5,3,6,4,2,18,4])
print(res)