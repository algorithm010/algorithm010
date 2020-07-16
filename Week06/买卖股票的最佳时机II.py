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