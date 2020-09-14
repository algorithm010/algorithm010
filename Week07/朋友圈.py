# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 10:58 PM

from typing import List


class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        if not nums: return 0
        def find(x):
            node = x
            while parent[node] != -1:
                node = parent[node]
            return node
        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:#如果根节点一致，结束此次
                return
            # parent[y_root] = x_root
            if rank[x_root] > rank[y_root]: parent[y_root] = x_root
            elif rank[y_root] > rank[x_root]: parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root] += 1
        size = len(nums)
        parent = [-1] * size
        rank = [0] * size
        for i in range(size):
            for j in range(size):
                if i != j and nums[i][j] == 1:
                    union(i, j)
        count = 0
        for i in parent:
            if i < 0:
                count += 1
        return count

nums = [[1,1,0],
 [1,1,0],
 [0,0,1]]
s = Solution()
res = s.findCircleNum(nums)
print(res)