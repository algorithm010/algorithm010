# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 7:44 PM

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if not nums: return 1
        # hashmap = {}
        # max_val = float('-inf')
        # for num in nums:
        #     if num > 0:
        #         hashmap[num] = hashmap.get(num,0)+1
        #     if num > max_val:
        #         max_val = num
        # if not hashmap: return 1
        # for num in range(1,max_val):
        #     if not hashmap.get(num):
        #         return num
        # return max_val + 1

        size = len(nums)
        for i in range(size):#将所有负值赋值为N+1
            if nums[i] <= 0:
                nums[i] = size + 1#后面不需要管这些显然大于数组长度的数值
        for i in range(size):
            ind = abs(nums[i])
            if ind <= size:
                nums[ind - 1] = -abs(nums[ind - 1])
        for i in range(size):
            if nums[i] > 0:
                return i + 1

        return size + 1

        # print(nums)
s = Solution()
nums = [-1,2,1,4,6,7]
print(nums)
s.firstMissingPositive(nums)
