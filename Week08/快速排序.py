# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 8:31 PM


# 快速排序的思想是在数组中找一个pivot使得左边比pivot小，右边比pivot大，然后对左右两侧元素同逻辑处理
# 也是不稳定的
class Solution:
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        ind = left + ((right-left) >> 1)
        pivot = self.partition(nums, left, right, nums[ind])
        self.quick_sort(nums, left, pivot-1) #左
        self.quick_sort(nums, pivot, right) #右

    def partition(self, nums, left, right, pivot):
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        return left



s = Solution()
nums = [2,3,1,4,2,5,6,8,6,5,7]
s.quick_sort(nums,0,len(nums)-1)
print(nums)