# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/16 12:15 AM

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def subRob(nums):
            pre_max, cur_max = 0, 0
            for i in range(len(nums)):
                pre_max, cur_max = cur_max, max(cur_max, pre_max + nums[i])
            return cur_max

        if not nums: return 0
        # a = subRob(nums[:-1])#抛除最后一个
        # b = subRob(nums[1:])
        return max(subRob(nums[:-1]),subRob(nums[1:])) if len(nums) != 1 else nums[0]

s = Solution()
res = s.rob([1])
print(res)