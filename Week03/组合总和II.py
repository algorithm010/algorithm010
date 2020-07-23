# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/24 12:42 AM

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, tmp, start):
            if target < 0: return
            if target == 0: res.append(tmp)
            # visited = set()
            for i in range(start, len(candidates)):
                if i > 0 and candidates[i-1] == candidates[i]: continue
                cur = candidates[i]
                # if cur in visited: continue
                # visited.add(cur)
                dfs(candidates[:i]+candidates[i+1:],target-cur,tmp+[cur],i)
        candidates.sort()
        res = []
        dfs(candidates,target,[],0)
        return res

s = Solution()
# candidates = [10,1,2,7,6,1,5]
candidates = [1,1,2,5,6,7,10]
target = 8
res = s.combinationSum2(candidates,target)
print(res)