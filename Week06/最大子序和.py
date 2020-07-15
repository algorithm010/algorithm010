# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/14 8:28 PM

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0], max_val = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_val = max(dp[i], max_val)
        # return max(dp)
        return max_val


s = Solution()
res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)
