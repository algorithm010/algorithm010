# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/30 3:08 AM

from typing import List
class Solution:
    def searchRangeI(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        def search(left, right, bound):
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    if bound == 0:
                        if mid == bound or nums[mid - 1] != target:
                            return mid
                        else: right = mid - 1
                    else:
                        if mid == bound or nums[mid+1] != target:
                            return mid
                        else: left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        size = len(nums)
        p1 = search(0, size - 1, 0)
        p2 = search(0, size - 1, size - 1)
        return [p1,p2]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1.要考虑到如果该数字不存在的情形
        if not nums: return [-1, -1]
        def search_left(left,right):
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                    else: right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        def search_right(left,right):
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    if mid == size-1 or nums[mid+1] != target:
                        return mid
                    else: left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        size = len(nums)
        p1 = search_left(0,size-1)
        p2 = search_right(0,size-1)
        return [p1,p2]
s = Solution()
nums = [5,7,7,8,8,10]
# nums = [1]
res = s.searchRangeI(nums,8)
print(res)