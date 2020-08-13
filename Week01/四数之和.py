# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 10:49 PM

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)#[-2,-1,0,0,1,2]
        if size < 4: return []
        res = []
        nums.sort()
        for i in range(size - 2):
            if i>0 and nums[i] == nums[i-1]: continue#确保不会和前面产生的结果重复
            if nums[i] * 4 > target: break
            for j in range(i + 1, size - 1):
                if j > i+1 and nums[j] == nums[j-1]: continue
                if nums[i] + nums[j]*3 > target: break
                left, right = j + 1, size - 1
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur == target:#注意下面的是while条件而不是if
                        while left < right and nums[left] == nums[left+1]: left = left + 1
                        while left < right and nums[right] == nums[right-1]: right = right -1
                        tmp =[nums[i],nums[j],nums[left],nums[right]]
                        res.append(tmp)
                        left, right = left + 1, right - 1
                    elif cur < target:
                        left += 1
                    else:
                        right -= 1
        return res

s = Solution()
# nums = [1, 0, -1, 0, -2, 2]
# nums = [-3,-2,-1,0,0,1,2,3]
nums = [4,-9,-2,-2,-7,9,9,5,10,-10,4,5,2,-4,-2,4,-9,5]
res = s.fourSum(nums,-13)
print(res)



