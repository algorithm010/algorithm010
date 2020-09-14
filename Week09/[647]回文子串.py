# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/19 12:52 AM

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        size = len(s)
        dp = [[True]*size for i in range(size)]
        count = 0
        for l in range(size):
            for i in range(size):
                j = i + l
                if j >= size: break
                if l == 0: dp[i][j] = True
                elif l == 1: dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j]:
                    count += 1
        return count