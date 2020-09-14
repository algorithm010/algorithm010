# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 11:37 AM

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #n个a，a 超时，这个过程不断的取一截，就很费操作
        # 用滑动窗口试一下
        m, n = len(s), len(p)
        res = []
        for i in range(m-n+1):
            cur = s[i:i+n]
            #判断此时的cur和p是否是异位词
            if self.isAngrams(cur,p): res.append(i)
        return res
    def isAngrams(self,s,p):
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1
        for ch in p:
            hashmap[ch] = hashmap.get(ch,0) - 1
        for key,value in hashmap.items():
            if value !=0 : return False
        return True

    def findAnagramsI(self, s: str, p: str) -> List[int]:
        from collections import deque
        m, n = len(s), len(p)
        hashmap = {}
        for ch in p:
            hashmap[ch] = hashmap.get(ch,0) + 1
        quene = deque()# 滑动窗口
        hashmap1 = {}
        res = []
        # s: "cbaebabacd"
        # p: "abc"
        for i in range(m+1):
            if len(quene) == n:
                if hashmap == hashmap1:
                    res.append(i-n)
                left = quene[0]
                if hashmap1[left] > 1:
                    hashmap1[left] -= 1
                else:
                    del hashmap1[left]
                quene.popleft()
            if i < m:
                ch = s[i]
                quene.append(ch)
                hashmap1[ch] = hashmap1.get(ch, 0) + 1
        return res
s = Solution()
# s1 = "cbaebabacdc"
# s2 = "abc"
s1 = "abab"
s2 = "ab"
res = s.findAnagramsI(s1,s2)
print(res)




