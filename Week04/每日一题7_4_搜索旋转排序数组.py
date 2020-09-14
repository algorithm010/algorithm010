# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/6 12:12 AM

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)>>1
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:#用两个点夹住target
                    right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:#用两个点夹住target
                    left = mid + 1
                else: right = mid - 1
        return  -1