# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 2:37 AM

class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        def dfs(cur, k, tmp, start):
            if k < 0: return
            if cur == target and k==0 : res.append(tmp)
            # visited = set()
            for i in range(start, 10):
                # if i in visited: continue
                # visited.add(i)
                dfs(cur+i,k-1,tmp+[i],i+1)
        res = []
        dfs(0,k,[],1)
        return res