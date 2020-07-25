# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/25 2:22 AM

from typing import  List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # def dfs(cur,tmp):
        #     if cur > target: return
        #     if cur == target: res.append(tmp)
        #     for i in range(len(nums)):
        #         dfs(cur+nums[i],tmp+[nums[i]])
        # res = []
        # dfs(0,[])
        # return len(res)
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]#这句话是有可能访问越界的
        return dp[-1]

s = Solution()
res = s.combinationSum4([1,2,4],7)
print(res)