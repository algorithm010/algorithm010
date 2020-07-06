# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/3 10:08 PM

class Solution:
    #1.贪心法
    def findContentChildren(self, A: List[int], B: List[int]) -> int:
        A.sort()#胃口
        B.sort()#饼干value
        #优先满足胃口小的孩子
        res = 0
        i, j = 0, 0
        while j < len(B) and i < len(A):
            if B[j]>=A[i]:#如果当前值大于胃口值
                res = res + 1
                i = i + 1
            j = j + 1
        return res