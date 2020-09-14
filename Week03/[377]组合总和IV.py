# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 2:39 AM

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dfs超时了
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
                    dp[i] += dp[i-nums[j]]
        return dp[-1]