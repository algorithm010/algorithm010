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
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # 超时了 时间复杂度是O(KN),空间复杂度是O(K)
        # if not nums or k == 0: return []
        # if k == 1: return nums
        # res = []
        # for i in range(len(nums)-k+1):
        #     cur = nums[i:i+k]
        #     res.append(max(cur))
        # return res
        if not nums or k == 0: return []
        if k == 1: return nums
        res = []
        quene = deque()
        for i in range(len(nums)):
            while quene and nums[i] > nums[quene[-1]]:
                quene.pop()
            # 使用双端队列 考虑何时进何时出
            # 进的规则是，如果队列里没有元素，直接进
            # 如果队列里有元素，如果此时的元素大，就把队列里的元素抛出,再把这个值入对
            # 如果一直都是更大的进来，队列首部的应该移除
            quene.append(i)  # 把这个元素的下标记录下来
            if i - quene[0] == k:
                quene.popleft()
            if i + 1 >= k:  # 有k个元素了，把nums[i-k:i]的最大值放进res，也就是quene[0]
                res.append(nums[quene[0]])  # 应该把此时队首的值放入res中
        return res


# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(res)