# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 1:37 PM

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # pass
        # 左右指针对撞， 如果 相同就向中心靠拢
        # 如果不等，就left++ 或者right--，判断是否是回文
        def check(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return check(left + 1, right) or check(left, right - 1)
        return True

