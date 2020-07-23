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


from typing import List
class SolutionII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums,tmp):
            if len(tmp) == size:
                res.append(tmp[:])
            visited = set()#同层去重，每一层只能选择这一层还没有被选过的元素
            for i in range(len(nums)):
                if nums[i] in visited: continue
                visited.add(nums[i])
                backtrace(nums[:i]+nums[i+1:],tmp+[nums[i]])
        res, size = [], len(nums)
        backtrace(nums,[])
        return res
s = SolutionII()
res = s.permuteUnique([1,1,2])
print(res)