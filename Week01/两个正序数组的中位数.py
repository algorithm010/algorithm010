# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 2:45 AM

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            p1, p2 = 0, 0
            while True:
                # 特殊情况
                if p1 == m:#如果一个数组为空
                    return nums2[p2 + k - 1]
                if p2 == n:
                    return nums1[p1 + k - 1]
                if k == 1:
                    return min(nums1[p1], nums2[p2])

                # 正常情况
                ind1 = min(p1 + k // 2 - 1, m - 1)#原数组a的第k//2个元素
                ind2 = min(p2 + k // 2 - 1, n - 1)#原数组b的第k//2个元素
                pivot1, pivot2 = nums1[ind1], nums2[ind2]
                if pivot1 <= pivot2:#删除较小数组的左侧k//2个元素，更新k值
                    k -= ind1 - p1 + 1
                    p1 = ind1 + 1
                else:
                    k -= ind2 - p2 + 1
                    p2 = ind2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength & 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

        #归并法 时间复杂度O(M+N)
        # nums = []
        # m, n = len(nums1), len(nums2)
        # size = m + n
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         nums.append(nums1[i])
        #         i = i + 1
        #     else:
        #         nums.append(nums2[j])
        #         j = j + 1
        # while i < m:
        #     nums.append(nums1[i])
        #     i = i + 1
        # while j<n:
        #     nums.append(nums2[j])
        #     j = j + 1
        # return nums[size//2] if size%2 == 1 else (nums[size//2]+nums[size//2-1])/2
s = Solution()
nums1 = [1, 2]
nums2 = [3,4]
res = s.findMedianSortedArrays(nums1,nums2)
print(res)