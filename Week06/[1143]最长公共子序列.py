# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/13 11:08 PM

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == '' or text2 == '': return 0
        m, n = len(text1), len(text2)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

s = Solution()
text1 = "abcde"
text2 = "ace"
res = s.longestCommonSubsequence(text1,text2)
print(res)