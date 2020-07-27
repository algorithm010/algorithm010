# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 9:46 PM

class Solution:
    def countBits(self, num: int) -> List[int]:
        # res = []
        # for i in range(num+1):
        #     count = 0
        #     while i!=0:
        #         i = i &(i-1)#消除末尾1
        #         count += 1
        #     res.append(count)
        # return res
        #动态规划 dp[n] = dp[n//2] + 1 if odd else + 0
        dp = [0] * (num + 1)
        for i in range(1, num + 1):  # 0不用处理
            dp[i] = dp[i >> 1] + (i & 1)
        return dp