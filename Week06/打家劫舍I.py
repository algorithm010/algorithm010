# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/15 11:13 PM

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(nums, i):
        #     if i >= len(nums):
        #         return 0
        #     # next1 = dfs(nums, start + 1)  # 不打劫，去下家
        #     # next2 = dfs(nums, start + 2) + nums[start]  # 打劫这一家
        #     # res = max(next1, next2)
        #     res = max(dfs(nums,i+1),dfs(nums,i+2)+nums[i])
        #     return res
        # return dfs(nums, 0)
        # if not nums: return 0
        # dp = [[0]*2 for _ in range(len(nums))]
        # dp[0][0],dp[0][1] = 0, nums[0]
        # for i in range(1,len(nums)):
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][1])#i不偷，那么i-1可偷可不偷
        #     dp[i][1] = dp[i-1][0] + nums[i]#确定i偷，那么i-1不偷
        # return max(dp[-1][0],dp[-1][1])

        # i偷的max_val = max(f(i-1),f(i-2)+nums[i])
        # if not nums: return 0
        # dp = [0]*(len(nums)+1)
        # dp[1] = nums[0]
        # for i in range(2,len(nums)+1):
        #     dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        # return dp[-1]
        pre_max, cur_max = 0, 0
        for i in range(len(nums)):
            # tmp = cur_max
            # cur_max = max(cur_max,nums+pre_max) #dp[i-1],dp[i-2]
            # pre_max = tmp
            pre_max, cur_max = cur_max, max(cur_max, pre_max + nums[i])
        return cur_max

s = Solution()
res = s.rob([2,3,1])
print(res)

