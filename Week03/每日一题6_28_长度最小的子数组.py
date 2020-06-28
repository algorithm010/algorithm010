# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/28 8:29 PM
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回
#  0。
#
#
#
#  示例：
#
#  输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
#
#
#  进阶：
#
#
#  如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#  Related Topics 数组 双指针 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # # 1. 穷举 超出时间限制
        # for i in range(1, len(nums) + 1):
        #     # 长度为1，2，3，穷举可能的解，找到则返回
        #     for j in range(len(nums) - i + 1):
        #         if sum(nums[j:i + j]) >= s: return i
        # return 0
        #2.双指针
        if not nums: return 0
        size, res = len(nums), len(nums) + 1
        start, end = 0, 0
        tmp = 0  # 记录窗口和
        while end < size:
            tmp = tmp + nums[end]
            while tmp >= s:  # 如果当前窗口和值大于s,收缩窗口
                res = min(res, end - start + 1)
                tmp = tmp - nums[start]
                start = start + 1
            end = end + 1  # 窗口扩张
        return 0 if end == size + 1 else res
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
# nums = [2,3,1,2,4,3]
nums = [1,2,3,4,5]
res= s.minSubArrayLen(1,nums)
print(res)