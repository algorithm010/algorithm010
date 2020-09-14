# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 8:08 PM

# 冒泡排序是稳定的
class Solution:
    def bubblesort(self,nums):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]


s = Solution()
nums = [2,3,1,4,2,5,6,8,6,5,7]
s.bubblesort(nums)
print(nums)