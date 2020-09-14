# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 11:08 AM


class Solution:
    def reverseOnlyLetters(self, strs: str) -> str:
        tmp = list(strs)
        left, right = 0, len(strs) - 1
        while left < right:
            while left < right and not tmp[left].isalpha():
                left = left + 1
            while left < right and not tmp[right].isalpha():
                right = right - 1
            tmp[left], tmp[right] = tmp[right], tmp[left]
            left, right = left + 1, right - 1
        return ''.join(tmp)