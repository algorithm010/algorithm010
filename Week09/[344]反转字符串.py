# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/7 10:44 PM

class Solution:
    def reverseString(self, strs: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(strs)
        left, right = 0, size-1
        while left < right:
            strs[left],strs[right] = strs[right],strs[left]
            left, right = left + 1, right - 1
        return strs