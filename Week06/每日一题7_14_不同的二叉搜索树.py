# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/15 12:41 AM


class Solution:
    def numTrees(self, n: int) -> int:
        # G = sum(F(I,N))
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]
