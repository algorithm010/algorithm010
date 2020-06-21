# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/14 11:03 PM

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#  说明:
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  要求使用空间复杂度为 O(1) 的 原地 算法。
#
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, nums, k):
        """
        要求原地置换
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 击败81%
        # k = k % len(nums)#要考虑k大于数组长度的情形
        # nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        # 击败64%
        tmp = nums[len(nums) - k:] + nums[:len(nums) - k]
        for i in range(len(tmp)):
            nums[i] = tmp[i]

        #暴力解法 超出时间限制
        for i in range(k%len(nums)):  # 旋转k次
            for j in range(len(nums) - 1, 0, -1):#反序调转
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

        # nums.reverse()
        # nums[:len(nums)-k].reverse()
#
# leetcode submit region end(Prohibit modification and deletion)

s =Solution()
a = [1,2,3,4,5,6,7]
s.rotate(a,2)
print(a)