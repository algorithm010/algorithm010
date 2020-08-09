# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/4 1:02 AM

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        # if size <= 2: return min(cost)
        # dp = [0] * size
        # dp[0], dp[1] = cost[0], cost[1]
        # for i in range(2,size):#要想到达最后一位，只可能是从i-1和i-2来的，所以总共的开销如下
        #     dp[i] = min(dp[i-1],dp[i-2])+cost[i]#到达i处花费的最少开销
        # return min(dp[-1],dp[-2])
        for i in range(2,size):
            cost[i] = min(cost[i-1],cost[i-2]) + cost[i]
        return min(cost[-1],cost[-2])