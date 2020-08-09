# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/14 9:15 PM

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp_min, dp_max = [0] * len(nums), [0] * len(nums)  # dp_max记录正负交替乘法中的最大值
        dp_min[0], dp_max[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                # 如果此时nums[i]大于0，如果之前是正数，那就乘上，如果是负数，那此时的最大值为此时的值
                dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i])
                # 此时原本小于0，最小值就应该乘上nums[i]；如果原本大于0，那最小的就应该是此时的值
                dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i])
            else:  # 此时nums[i]小于0
                # 如果原本dp_min小于0，它乘上num可能是最大值；如果原来是正值，(+值*负值和负值) 中要求大值
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res
        # dp_max = [1] * (len(nums)+1)
        # dp_min = [1] * (len(nums)+1)
        # for i in range(1, len(nums)+1):
        #     dp_max[i] = max(dp_max[i - 1] * nums[i-1], dp_min[i - 1] * nums[i-1], nums[i-1])
        #     dp_min[i] = min(dp_max[i - 1] * nums[i-1], dp_min[i - 1] * nums[i-1], nums[i-1])
        # return max(dp_max)



s = Solution()
# nums = [2,3,-2,-4]
# nums = [3,-1,4]
# nums = [0, 2]
# nums = [2,3,-2,4]
nums = [2,-5,-2,-4,3]
res = s.maxProduct(nums)
print(res)
