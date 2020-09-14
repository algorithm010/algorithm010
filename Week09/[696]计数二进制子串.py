# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/10 11:01 PM

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = [1]
        j = 0
        for i in range(1, len(s)):  # 统计连续的频数
            if s[i] == s[i - 1]:
                count[j] += 1
            else:
                count.append(1)
                j += 1
        res = 0
        for k in range(1, len(count)):
            res += min(count[k], count[k - 1])  # 取相邻频数的最小值
        return res

s = Solution()
strs = "001110011"
res = s.countBinarySubstrings(strs)
print(res)

