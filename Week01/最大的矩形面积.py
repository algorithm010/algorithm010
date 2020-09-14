# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/13 12:59 AM

# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
        # 1.暴力解 超出时间限制
        # size = len(heights)
        # res = 0
        # for i in range(size):
        #     left = i
        #     cur_height = heights[i]
        #     while left > 0 and heights[left - 1] >= cur_height:
        #         left -= 1
        #
        #     right = i
        #     while right < size - 1 and heights[right + 1] >= cur_height:
        #         right += 1
        #     res = max(res, (right - left + 1) * cur_height)
        # return res
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)#[2,1,5,6,2,3]
        res = 0
        stack = []
        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                # 如果当前height的右边height严格小于height，则确定了此轮的height
                cur_height = heights[stack.pop()]

                # while len(stack) > 0 and cur_height == heights[stack[-1]]:
                #     stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_height * cur_width)
            stack.append(i)#记录的是heights的下标

        while len(stack) > 0 is not None:#处理还未出栈的高度
            cur_height = heights[stack.pop()]
            # while len(stack) > 0 and cur_height == heights[stack[-1]]:#处理相邻高度一致的情形
            #     stack.pop()

            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)
        return res


class SolutionI:
    #哨兵优化 击败73%
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        size = len(heights)
        stack, res = [], 0
        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack.pop()]:
                cur_height = heights[stack.pop()]
                res = max(res, cur_height * (i - stack[-1] - 1))
            stack.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.largestRectangleArea([2,1,5,6,2,3])
print(res)