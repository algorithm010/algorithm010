# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 9:44 PM

#
#
# @param n int整型
# @param m int整型
# @param a int整型一维数组
# @return int整型
#
class Solution:
    def solve(self, n, m, nums):
        # write code here
        # 6,1, [1,0,0,1,1,1]
        # 设dp[i][j]是第i次染色，到第j块能拿到的最大板子长度
        # dp[0] = nums[:]
        #  dp[i][0] = 1
        # for i in range(1,m+1)
        # dp[i][j] = max(dp[i-1][j],dp[i][j-1]+1)


s = Solution()
nums = [1,0,0,1,1,1]
res = s.solve(6,2,nums)
print(res)