# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 1:36 AM

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, size = 0, len(nums)
        for i in range(size):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        return left


s = Solution()
nums = [0,1,2,2,3,0,4,2]
res = s.removeElement(nums,2)
print(nums)