# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/30 12:19 AM

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, strs: str, words: List[str]) -> List[int]:
        if not words: return []
        size = len(words[0])#单词长度
        if size > len(strs): return []
        res, tmp = [], {}
        for word in words:
            tmp[word] = tmp.get(word, 0) + 1
        #利用words全部元素构造为strs的一个连续串
        for i in range(len(strs)):
            j = i
            hashmap = tmp.copy()
            # 这里可以考虑用两个hashmap来做，匹配的时候先将words长度的字符串搞出来
            while strs[j:j+size] in hashmap:
                cur = strs[j:j+size]
                hashmap[cur] -= 1
                if hashmap.get(cur) == 0:
                    hashmap.pop(cur)
                j = j+size
            if len(hashmap) == 0:#现在判断条件需要修改 不再是长度为0，而是字典里面value全是0
                res.append(i)
        return res
    def findSubstringII(self, s, words):
        if not words: return []
        k = len(words[0])
        res = []
        tmp = Counter(words)
        for left in range(k):#k组
            hashmap = tmp.copy()
            for right in range(left + k, len(s) + 1, k):#滑动k
                word = s[right - k: right]#截取出原串中的部分
                hashmap[word] -= 1#这句话不会报错么？？？？
                while hashmap[word] < 0:
                    hashmap[s[left:left + k]] += 1
                    left += k
                if left + k * len(words) == right:
                    res.append(left)
        return res


s = Solution()
# strs = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
strs = "barfoothefoobarman"
words = ["foo","bar"]
res = s.findSubstringII(strs,words)
print(res)