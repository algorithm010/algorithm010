# # -*- coding:utf-8 -*-
# # Author : Ray
# # Data : 2020/7/28 8:44 PM
#
# 归并排序的思想是将数组分作AB两区，AB两区都区内有序之后，合并这两个区
# 如果归并的时候 有相同的值，将左侧的放到tmp中就是稳定的
class Solution:
    def merge_sort(self, nums):
        if len(nums)<2:
            return nums
        mid = len(nums)//2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        return self.merge(self.merge_sort(nums1), self.merge_sort(nums2))

    def merge(self, nums1, nums2):
        res = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))
        while nums1:
            res.append(nums1.pop(0))
        while nums2:
            res.append(nums2.pop(0))
        return res


s = Solution()
nums = [2,3,1,4,2,5,6,8,6,5,7]
res = s.merge_sort(nums)
print(res)


