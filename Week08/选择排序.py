# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 8:17 PM


# 选择排序的思想是分作AB两区，A一直有序，每次从B中取出最小的元素，放在A区
class Solution:
    def insertsort(self,nums):
        for i in range(len(nums)-1):
            min_loc = i
            for j in range(i+1,len(nums)):#找到B区最小的元素
                if nums[min_loc] > nums[j]:
                    min_loc = j
            nums[i],nums[min_loc] = nums[min_loc],nums[i]

s = Solution()
nums = [2,3,1,4,2,5,6,8,6,5,7]
s.insertsort(nums)
print(nums)