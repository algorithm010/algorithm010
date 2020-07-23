# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/23 9:45 PM

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0: return False
        # tmp = str(x)
        # left,right = 0, len(tmp)-1
        # while left <= right:
        #     if tmp[left] != tmp[right]: return False
        #     else: left,right = left+1,right-1
        # return True

        # return str(x) == str(x)[::-1]
        res = x
        tmp = 0
        while x > 0:
            tmp = tmp*10 + x%10
            x = x//10
        return res == tmp
s = Solution()
res = s.isPalindrome(-1211)
print(res)
