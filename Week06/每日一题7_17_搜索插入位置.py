# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/17 11:58 PM

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums : return 0
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left)//2#防溢出
            if nums[mid] == target: return mid
            elif nums[mid] > target:right = mid - 1
            else: left = mid + 1
        return left
