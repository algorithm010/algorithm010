# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/5 12:31 AM

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        tmp = ''
        for ch, times in hashmap.items():
            if times == 1:
                tmp = ch
                break
        if not tmp:
            return -1
        else:
            return s.index(ch)

