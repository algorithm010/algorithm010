# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/13 10:04 AM
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
#
#  返回滑动窗口中的最大值。
#
#
#
#  进阶：
#
#  你能在线性时间复杂度内解决此题吗？
#
#
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^4 <= nums[i] <= 10^4
#  1 <= k <= nums.length
#
#  Related Topics 堆 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1.暴力解
        # res = []
        # for i in range(0, len(nums) - k + 1):
        #     window = nums[i:i+k]
        #     res.append(max(window))
        # return res
        # return [max(nums[i:i + k]) for i in range(n - k + 1)]


from collections import deque
class SolutionII:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        #双端队列 击败30%
        size = len(nums)
        if size == 0 or k == 0:
            return []
        if k == 1:
            return nums
        def ope_deque(i):
            if deq and deq[0] == i-k: # [7,2,4],2 滑动过程中，将window的最左元素出掉
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:# 整体上滑动的过程还是一个先进先出队列的形式
                deq.pop()
        max_index = 0
        deq = deque()
        res = []
        for i in range(k):
            ope_deque(i)
            deq.append(i)
            if nums[i] > nums[max_index]:
                max_index = i
        res.append(nums[max_index])

        for i in range(k,size):
            ope_deque(i)
            deq.append(i)
            res.append(nums[deq[0]])#窗口开始滑动，要记录此时窗口的最大值
        return res
# leetcode submit region end(Prohibit modification and deletion)


s = SolutionII()
res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(res)