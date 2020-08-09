# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/23 11:53 PM

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, tmp, start):
            if target<0: return
            if target == 0:
                res.append(tmp)
            # for num in candidates:
            #     dfs(candidates, target-num, tmp+[num])
            for i in range(start, len(candidates)):
                dfs(candidates, target-candidates[i], tmp+[candidates[i]], i)
        res = []
        dfs(candidates, target, [], 0)
        return res
        # res = [sorted(nums) for nums in res]
        # res = [nums for nums in res if nums not in res]

s = Solution()
candidates = [2,3,6,7]
target = 7
res = s.combinationSum(candidates,target)
print(res)