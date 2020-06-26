# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 10:27 PM

from typing import List
class Solution(object):
    # def permute(self, nums):
        # def backtracing(first=0):
        #     if first == size:
        #         result.append(nums[:])
        #     for i in range(first, size):
        #         nums[first], nums[i] = nums[i], nums[first]
        #         backtracing(first+1)
        #         nums[first], nums[i] = nums[i], nums[first]

        # size = len(nums)
        # result = []
        # #l路径
        # #选择列表 就是除去已经被加入到cur中的其余元素
        # backtracing()
        # return result
    # def permute(self,nums):
    #     res = []
    #     self.backtracing(res,nums,[])
    #     return res
    # def backtracing(self,res,nums,tmp):
    #     #触发结束条件
    #     if len(nums) == len(tmp):
    #         res.append(tmp[:])
    #         # return #返回上一层调用
    #     for i in range(len(nums)):
    #         #排除不合法的，处理了好多
    #         if nums[i] in tmp: continue
    #         #做选择
    #         tmp.append(nums[i])
    #         #进入下一层
    #         self.backtracing(res,nums,tmp)
    #         tmp.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums, tmp):
            #触发结束条件
            if not nums:
                res.append(tmp[:])
            for i in range(len(nums)):
                #排除不合法或已存在的
                if nums[i] in tmp: continue
                #做选择 修改已选路径和能选择的路径
                #进入下一次决策、回溯之前的决策
                backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])#修改选择项和路径
        res = []
        backtrace(nums, [])
        return res




s = Solution()
nums = [1,3,2]
res = s.permute(nums)
print(res)