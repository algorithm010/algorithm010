# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/25 8:39 AM

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#
#
#  示例：
#
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 10^3
#  -10^3 <= nums[i] <= 10^3
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # 先排序
        # [-4,-1,1,2],1
        min_closer = float('inf')
        for i in range(len(nums) - 2):  # 为双指针留出位置
            if i > 0 and nums[i] == nums[i - 1]:  # 保证前后两个数字不一，因为只有一组解
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]  # 先记录当前遍历得到的三数之和
                if abs(min_closer - target) > abs(tmp - target):
                    min_closer = tmp
                # min_closer = min(abs(target-tmp),min_closer)
                if tmp < target:  # 如果还没有找到相等的 ，j右移
                    left = left + 1
                    # cur_diff = abs()
                elif tmp > target:  # 如果找着找着 大于target了，就需要和之前记录的min_diff比较
                    right = right - 1
                else:  # tmp==target:
                    return min_closer
        return min_closer

# leetcode submit region end(Prohibit modification and deletion)
