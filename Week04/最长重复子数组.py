# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/1 10:06 PM

from  typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                k = 0
                while i+k < len(a) and j+k < len(B) and A[i+k] == B[j+k]:
                    k = k + 1
                res = max(res,k)
        return res

s = Solution()
a = [1,2,3,2,1]
b = [3,2,1,4,7]
res = s.findLength(a,b)
print(res)


