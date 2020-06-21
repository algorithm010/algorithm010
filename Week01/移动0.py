# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/8 11:43 PM

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        1.遇到0将该0添加至末尾，然后删除数组首部的0，由于移除0的时间复杂度为o(N)，故而整体的时间复杂度为O(N^2)
        2.统计0的个数，遍历过程中碰到不为0的数，就将它向前挪动count位
        3.双指针，分别记录等于0的下标和不等于0的下标，交换值
        4.遍历过程中碰上等于0的数，与其后面的元素进行交换
        """
        # 击败7%
        # for num in nums:
        #     if num == 0:
        #         nums.append(0)
        #         nums.remove(0)
        # 击败68%
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         count = count + 1
        #     else:#[0,1,0,3,12]
        #         nums[i-count] = nums[i]
        # for i in range(len(nums)-count,len(nums)):
        #     nums[i] = 0
        # 击败94%
        # index_0 = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         if i != index_0:
        #             nums[index_0], nums[i] = nums[i], 0
        #         index_0 = index_0 + 1
        # 击败98%
        index_0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index_0], nums[i] = nums[i], nums[index_0]
                index_0 = index_0 + 1

        return nums


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.moveZeroes([0,1,0,3,12])
print(res)