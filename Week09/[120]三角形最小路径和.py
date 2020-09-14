# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/3 1:57 AM

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 分治 递归模板
        # from functools import lru_cache
        # @lru_cache(None)
        # def dfs(i, j):
        #     #terminator
        #     if i == size-1: return triangle[i][j]
        #     left = dfs(i+1,j)#加左边的值
        #     right = dfs(i+1,j+1)
        #     min_val = min(left, right) + triangle[i][j]
        #     return min_val
        # size = len(triangle)
        # return dfs(0,0)
        # 2.top-down
        # if not triangle: return
        # dp = triangle
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             dp[i][j] += triangle[i-1][j]
        #         elif j == len(triangle[i])-1:
        #             dp[i][j] += triangle[i-1][j-1]
        #         else:
        #             dp[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        # return min(dp[-1])
        # 3.bottom-up
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
