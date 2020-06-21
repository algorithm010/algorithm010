# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 4:13 PM

# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明:
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例:
#
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #击败99.9% 占用额外空间
        # nums1[:] = sorted((nums1[:m] + nums2))
        #击败70% 双指针+ 额外空间 从头开始比较
        # tmp = nums1[:m]
        # nums1[:] = []
        # i, j = 0, 0
        # while i < m and j < n:
        #     if tmp[i] < nums2[j]:
        #         nums1.append(tmp[i])
        #         i = i + 1
        #     else:
        #         nums1.append(nums2[j])
        #         j = j + 1
        # if i < m:#tmp数组中还有剩余元素
        #     nums1[i+j:] = tmp[i:]
        # if j < n:
        #     nums1[i+j:] = nums2[j:]
        #时间复杂度是O(m+n),空间开销是常数级
        i, j = m-1, n-1
        ind = m+n-1
        while i >= 0 and j >= 0:#从后往前比较，将较大的值存入nums1末尾中
            if nums1[i] > nums2[j]:
                nums1[ind] = nums1[i]
                ind, i = ind-1, i-1
            else:
                nums1[ind] = nums2[j]
                ind, j = ind-1, j-1
        #如果nums1中还有元素不需要处理
        #而如果是nums2中还有元素，那么说明nums1中前面的元素需要被替换
        nums1[:j+1] = nums2[:j+1]
        return nums1
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.merge([1,2,3,0,0,0],3,[0,1,5],3)
print(res)