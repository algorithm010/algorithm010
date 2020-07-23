# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/23 8:26 PM

#给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrace(first=1, tmp=[]):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(first,n+1):
                tmp.append(i)
                backtrace(i+1, tmp)
                tmp.pop()
        res = []
        backtrace()
        return res


s = Solution()
res = s.combine(4,3)
print(res)