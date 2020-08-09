# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/5 12:31 AM

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        for i in range(len(s)):
            if hashmap.get(s[i]) == 1:
                return i
        return -1
        # 这里我是用hashmap中times=1的ch反向查找字符串 这里的时间复杂度就是O(MN)了
        # tmp = ''
        # for ch, times in hashmap.items():
        #     if times == 1:
        #         tmp = ch
        #         break
        # if not tmp:
        #     return -1
        # else:
        #     return s.index(ch)
        # 更好的做法应该是再遍历字符串，检查其times是否为1即可


