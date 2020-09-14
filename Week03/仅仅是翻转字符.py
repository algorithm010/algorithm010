# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/23 8:59 PM

class Solution:
    def reverseOnlyLetters(self, strs: str) -> str:
        tmp = list(strs)
        left, right = 0, len(strs) - 1
        while left <= right:
            if not tmp[left].isalpha(): left = left + 1
            elif not tmp[right].isalpha(): right = right - 1
            else:
                tmp[left], tmp[right] = tmp[right], tmp[left]
                left, right = left + 1, right - 1
        return ''.join(tmp)

s = Solution()
strs = "a-bC-dEf-ghIj"
# strs = "ab-cd"
# strs = "7_28]"
res = s.reverseOnlyLetters(strs)
print(res)