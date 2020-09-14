# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 8:15 PM


# 插入排序的思想是，假设数组分作两区，A区一直有序，每次从B区中取出元素，插入A区的合适位置
# 所以是不稳定的
class Solution:
    def insertsort(self, nums):
        for i in range(1,len(nums)):
            tmp, j = nums[i], i - 1#j要在A区中找到合适位置【往前找】，同时还要挪动其他元素
            while j >= 0 and nums[j] > tmp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = tmp



s = Solution()
nums = [2, 3, 1, 4, 2, 5, 6, 8, 6, 5, 7]
s.insertsort(nums)
print(nums)
