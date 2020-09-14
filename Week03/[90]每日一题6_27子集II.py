# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/12 8:35 PM
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first=0,tmp=[]):
            res.append(tmp[:])
            for i in range(first,size):
                if i > first and nums[i] == nums[i-1]: continue
                tmp.append(nums[i])
                backtrace(i + 1, tmp)
                tmp.pop()
        res, size = [], len(nums)
        nums.sort()
        backtrace()
        return res
s = Solution()
res = s.subsetsWithDup([4,4,4,1,4])
print(res)
print(len(res))

