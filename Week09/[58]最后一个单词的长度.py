# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/4 11:52 PM

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.split()
        # if not s: return 0 #去除全部是空格
        # return len(s[-1])
        p1 = len(s)-1
        while p1 >= 0 and s[p1] == ' ':#先略过末尾的空格
            p1 -= 1
        if p1 == -1: return 0#全部为空格
        p2 = p1
        while p2 >= 0 and s[p2] != ' ':#从后向前找到第一个不为空格的字符
            p2 -= 1
        return p1 - p2

s = Solution()
strs = "Hello  World "
res = s.lengthOfLastWord(strs)
print(res)