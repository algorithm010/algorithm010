# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 11:10 AM

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1
        for ch in t:
            hashmap[ch] = hashmap.get(ch,0) - 1
        for key,val in hashmap.items():
            if val != 0: return False
        return True