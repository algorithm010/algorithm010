# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/1 11:50 PM

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #1.暴力法 超出时间限制O(N^2)
        res = 0
        for i in range(len(prices)-1,0,-1):
            for j in range(i-1,-1,-1):
                diff = prices[i]-prices[j]#计算差值
                if diff > 0:
                    res = max(res,diff)
        return res

    def maxProfitI(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit



s = Solution()
nums = [7,1,5,3,6,4]
res = s.maxProfitI(nums)
print(res)