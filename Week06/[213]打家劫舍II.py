# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/16 12:15 AM

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #在上一题优化空间解法的基础上很容易理解
        def subRob(nums):
            pre_max, cur_max = 0, 0
            for i in range(len(nums)):
                pre_max, cur_max = cur_max, max(cur_max,pre_max+nums[i])
            return cur_max
        if not nums: return 0
        #取两种偷法里的最大值 不偷最后一个房子和不偷第一个房子
        return max(subRob(nums[:-1]), subRob(nums[1:])) if len(nums) != 1 else nums[0]
s = Solution()
res = s.rob([1])
print(res)