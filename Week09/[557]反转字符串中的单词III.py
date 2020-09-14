# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 10:52 AM

# 组内翻转单词

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res= [''.join(reversed(item)) for item in s]
        return ' '.join(res)