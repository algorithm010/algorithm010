# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 1:31 PM

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # tmp = ''.join(ch.lower() for ch in s if ch.isalnum())
        # return tmp == tmp[::-1]
        tmp = ''.join(ch.lower() for ch in s if ch.isalnum())
        # print(tmp)
        left, right = 0, len(tmp)-1
        while left <= right:
            if tmp[left] != tmp[right]:
                return False
            left, right = left + 1, right - 1
        return True
s = Solution()
strs = "A man, a plan, a canal: Panama"
res = s.isPalindrome(strs)
print(res)