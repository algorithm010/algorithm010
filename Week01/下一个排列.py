# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/29 11:40 PM

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.从后往前，找到第一个nums[i]<nums[i+1]的下标i
        # 2.从后往前，找到第一个比nums[i]大的元素nums[k]
        # 3.交换nums[i] nums[k]
        # 4.reverse nums[i+1:]
        p1, size = -1, len(nums)-1
        for i in range(size,-1,-1):#如果找不到,可以和面试官沟通这里怎么处理
            if nums[i-1] < nums[i]:
                p1 = i-1
                break
        if p1 == -1:
            return self.my_reverse(nums,p1+1,size)
        for i in range(size,p1-1,-1):
            if nums[i] > nums[p1]:
                nums[i], nums[p1] = nums[p1], nums[i]
                break
        return self.my_reverse(nums,p1+1,size)

    def my_reverse(self, nums, left, right):
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        return nums

s = Solution()
nums = [1,2,5,4,1]
# nums = [1,2,4,8,5,2,1]
# nums = [3,2,1]
res = s.nextPermutation(nums)
print(res)