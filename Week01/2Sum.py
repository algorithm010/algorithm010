# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 只用找到一组解的下标即可
        # 1.暴力解法：两重循环
        # 2.hash表记录 两次hash
        # 3.一次hash表
        # 击败18%
        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # 击败53%
        # dict = {}
        # for ind, num in enumerate(nums):  # 创建hash表
        #     dict[num] = ind
        # for ind, num in enumerate(nums):  # 遍历hash表
        #     j = dict.get(target - num)
        #     if j and ind != j:  # 排除[2,3] 4这种情况
        #         return [ind, j]
        # 击败78%
        dict = {}
        for ind, num in enumerate(nums):
            if dict.get(target - num) is not None:
                return [dict.get(target - num), ind]
            dict[num] = ind
# leetcode submit region end(Prohibit modification and deletion)
