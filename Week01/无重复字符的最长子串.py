# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/26 10:57 PM

class Solution:
    def lengthOfLongestSubstring(self, strs: str) -> int:
        # [a,b,c,a,b,c,d]
        # if not strs: return 0
        # quene = []
        # max_len, cur_len = 0,0
        # for ch in strs:
        #     while ch in quene:#O(N)
        #         quene.pop(0)#双端队列
        #         cur_len -= 1
        #     if ch not in quene:
        #         quene.append(ch)
        #         cur_len += 1
        #     max_len = max(max_len,cur_len)
        # return max_len
        # 很明显，记录长度的时候可以不需要使用队列，而是直接用右指针记录下一次的起始
        if not strs: return 0
        visited = set()
        max_len, cur_len, left = 0, 0, 0
        for i in range(len(strs)):
            while strs[i] in visited:
                visited.remove(strs[left])
                left = left + 1
                cur_len -= 1
            visited.add(strs[i])
            cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len


s = Solution()
strs = "abcabcbb"
res = s.lengthOfLongestSubstring(strs)
print(res)