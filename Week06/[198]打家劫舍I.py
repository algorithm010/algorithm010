# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/15 11:13 PM

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(nums, i):
        #     if i >= len(nums): return 0
        #     if nums[i] != -1: return nums[i]
        #     res = max(dfs(nums, i + 1), dfs(nums, i + 2) + nums[i])
        #     cache[i] = res  # 备忘录 防止超时
        #     return res
        # cache = [-1] * len(nums)
        # return dfs(nums, 0)

        # dp[i][0,1]偷到第i户人家 能得到的最大金额0偷，1不偷
        # dp[i][0,1] = max(dp[i-1][1]+nums[i],dp[i-1][0])
        # dp[i] 表示第i天偷能获得的最大金额
        # dp[i] = max(dp[i-2]+nums[i],dp[i-1])

        if not nums: return 0
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0],dp[0][1] = 0, nums[0]
        for i in range(1,len(nums)):
        # dp[i][0,1] 0不偷，1偷 如果i天偷，那么i-1不偷，而i天不偷，则可能是i-1不偷，也可能是i-1偷了
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])#i不偷，那么i-1可偷可不偷
            dp[i][1] = dp[i-1][0] + nums[i]#确定i偷，那么i-1不偷
        return max(dp[-1][0],dp[-1][1])

        # i偷的max_val = max(f(i-1),f(i-2)+nums[i])
        # if not nums: return 0
        # dp = [0]*(len(nums)+1)
        # dp[1] = nums[0]
        # for i in range(2,len(nums)+1):
        #     dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        # return dp[-1]

        # pre_max, cur_max = 0,0
        # for i in range(len(nums)):
        #     pre_max, cur_max = cur_max, max(cur_max,pre_max+nums[i])
        # return cur_max


s = Solution()
res = s.rob([2,3,1])
print(res)

