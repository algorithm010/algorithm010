# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 11:55 PM

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(nums, tmp):
            if not nums:
                res.append(tmp[:])
            visited = set()
            for i in range(len(nums)):
                if nums[i] in visited: continue#在每一层剪枝
                visited.add(nums[i])
                backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])#修改选择项和路径

        res = []
        backtrace(nums, [])
        return res
        # res = []
    #     self.backtracing(res,nums,[])
    #     return res
    # def backtracing(self,res,nums,tmp):
    #     #触发结束条件
    #     if len(nums)==len(tmp):
    #         res.append(tmp[:])
    #     for i in range(len(nums)):
    #         #排除不合法条件
    #         if nums[i] in tmp:
    #             continue
    #         #做选择
    #         tmp.append(nums[i])
    #         #进入下一层决策
    #         self.backtracing(res,nums,tmp)
    #         tmp.pop()
s = Solution()
res = s.permuteUnique([1,1,2])
print(res)