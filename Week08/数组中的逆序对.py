# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/2 8:07 PM

from typing import List
# 前有序数组中元素出列的时候，计算逆序个数

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        temp = [0 for _ in range(size)]
        return self.reverse_pairs(nums, 0, size - 1, temp)

    def reverse_pairs(self, nums, left, right, temp):#在数组 nums 的区间 [l,r] 统计逆序对
        if left == right:
            return 0
        mid = left + ((right-left) >> 1)
        lpairs = self.reverse_pairs(nums, left, mid, temp)
        rpairs = self.reverse_pairs(nums, mid + 1, right, temp)
        cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
        return lpairs + rpairs + cross_pairs

    def merge_and_count(self, nums, left, mid, right, temp):
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i,j,count = left, mid+1,0
        for k in range(left, right + 1):
            if i == mid + 1:#左侧处理完之后
                nums[k] = temp[j]
                j += 1
            elif j == right + 1:#右侧处理完之后
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:#前边的小，不用计数，将前边的值归并到temp中
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]#后边的小，将后边的值归并到tmp中，累计计数值
                j += 1
                count += (mid - i + 1)#
        return count


s = Solution()
res = s.reversePairs(nums=[5,2,6,1])
print(res)