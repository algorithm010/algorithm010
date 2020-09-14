# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/13 1:32 AM

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        cur = 0
        while cur<=right:#注意这里的循环条件
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                cur += 1
                left += 1
            elif nums[cur] == 2:
                nums[cur],nums[right] = nums[right],nums[cur]
                right -= 1
            else:
                cur += 1
        # return nums