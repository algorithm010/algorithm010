# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/4 1:39 AM

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        # if not nums: return 0
        # dp = [1]*len(nums)
        # 其实说白了就是暴力法的另外一种写法
        # 枚举起始点，看以它为终点的位置 上升子序列长度是多少，只不过比平常的暴力解法还是稍微简单一些
        # 以nums[i]为尾元素的最大子序列长度
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)
        size = len(nums)
        if size < 2: return size
        tmp = [nums[0]]  # 维护一个单调栈
        # 遍历数组，如果比末尾元素大，加入，如果小于等于 找到第一个比他大的数，替换掉
        for num in nums[1:]:
            if num > tmp[-1]:
                tmp.append(num)
            # [2,2,4] 3
            else:  # 在有序数组中找到第一个比num大的位置
                left, right = 0,len(tmp)-1
                while left <= right:
                    mid = left + ((right-left)//2)
                    if tmp[mid] >= num:
                        if mid == 0 or tmp[mid-1] < num:
                            tmp[mid] = num
                            break
                        else: right = mid - 1
                    else:
                        left = mid + 1

                # for i in range(len(tmp)):
                #     if tmp[i] == num:
                #         break
                #     elif tmp[i] > num:
                #         tmp[i] = num
                #         break
        print(tmp)
        return len(tmp)

s = Solution()
# nums = [10,9,2,5,3,7,101,18]
nums = [4,10,4,3,8,9]
res = s.lengthOfLIS(nums)
print(res)