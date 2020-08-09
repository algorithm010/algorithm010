# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 11:21 AM

class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for ch in strs:
            cur = ''.join(sorted(ch))
            hashmap[cur] = hashmap.get(cur,[]) + [ch]
        # print(hashmap)
        return [hashmap[item] for item in hashmap]