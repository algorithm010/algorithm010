# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/11 2:20 PM

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1.暴力法，三重循环
        # nums.sort()
        # res = set()
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for m in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[m] == 0:
        #                 res.add((nums[i],nums[j],nums[m]))
        # return list([list(item) for item in res])
        # 2.hash表+两重循环 击败5%
        hashmap = {}
        nums.sort()
        res = set()
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = 0 - nums[i] - nums[j]
                if hashmap.get(target) is not None and hashmap[target] > j:
                    # Only need to check if the target value on the right side of (j)
                    res.add((nums[i], nums[j], target))
        return list(res)

        # 外层循环+双指针 击败7%
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     left, right = i + 1, len(nums) - 1
        #     while left < right:
        #         if nums[left] == nums[left+1]:#[0,0,0]会报错
        #             left += 1
        #             continue
        #         tmp = nums[i] + nums[left] + nums[right]
        #         if tmp < 0:
        #             left += 1
        #         elif tmp > 0:
        #             right -= 1
        #         else:
        #             res.add((nums[i], nums[left], nums[right]))
        #             left, right = left + 1, right - 1
        # return list(res)

        # 外层循环+双指针 + 预处理去重 击败76%
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i]>0:#plus this line ,you can beat 93%
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while (left < right):
                tmp = nums[i] + nums[left] + nums[right]
                if tmp < 0:
                    left = left + 1
                elif tmp > 0:
                    right = right - 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    while (left < right) and nums[left] == nums[left + 1]:
                        left = left + 1
                    while (left < right) and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1 #put the two lines, you can
                    right = right - 1
        return res

        # leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# res = s.threeSum([-4,-1,-1,0,1,2])
res = s.threeSum([0,0,0])
print(res)