# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/29 12:34 AM

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        m, n = len(haystack), len(needle)
        for i in range(0,m-n+1):#5-2=3
            if haystack[i:i+n] == needle:
                return i
        return -1
        #刚开始想的时候就是用滑动窗口做，但是没写出来，反倒是这种直接暴力的反而简单
        # 滑动窗口关键在于 回溯
        # if not needle: return 0
        # m, n = len(haystack), len(needle)
        # p1 = p2 = 0
        # curr_len = 0
        # while p1 <= m - n:
        #     while p1 < m and haystack[p1] == needle[p2]:
        #         curr_len += 1
        #         p1 += 1
        #         p2 += 1
        #         if curr_len == n:
        #             return p1 - n
        #     # 回溯，移动pn到开始位置的后一位。重置其他变量
        #     p1 = p1 - curr_len + 1
        #     p2 = 0
        #     curr_len = 0
        # return -1


s = Solution()
haystack = "hello"
needle = "lo"
res = s.strStr(haystack,needle)
print(res)