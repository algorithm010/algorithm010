# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/9 10:23 PM

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例：
#
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 暴力 时间复杂度O(N^2) 运行不通过
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         area = (j - i) * min(height[j], height[i])
        #         if max_area < area: max_area = area
        # return max_area
        #击败84%的人
        left,right,area = 0,len(height)-1,0
        while left<right:
            if height[left] < height[right]:
                area = max(area,height[left]*(right-left))
                left += 1# 往右找看是否有较高的板子
            else:
                area = max(area,height[right]*(right-left))
                right -= 1
        return area


# leetcode submit region end(Prohibit modification and deletion)
