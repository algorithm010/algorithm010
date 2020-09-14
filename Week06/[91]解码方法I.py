# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/19 9:19 AM


class Solution:
    def numDecodings(self, s: str) -> int:
        size=len(s)
        if not s or s[0]=="0":
            return 0
        dp=[0]*(size+1)
        dp[0], dp[1] = 1, 1
        for i in range(1,size):
            if s[i]=="0":#如果当前位为0
                if s[i-1] == "1" or s[i-1] == "2":#它最多能与前一位合并，那时的解码方法等于dp[i-1]
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if '10'<=s[i-1:i+1]<='26':
                # if(s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")):
                    dp[i+1] = dp[i]+dp[i-1] # 等于上一个位置和上上个位置的解码方法和
                else:
                    dp[i+1] = dp[i]
        return dp[-1]

s = Solution()
res = s.numDecodings('1236')
print(res)