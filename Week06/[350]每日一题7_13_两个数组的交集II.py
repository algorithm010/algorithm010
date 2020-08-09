# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/13 11:40 PM

from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #1.hashmap 时间复杂度O(M+N),空间复杂度O(max(M,N)),可以优化为min
        # hashmap,res = {}, []
        # for num in nums1:
        #     hashmap[num] = hashmap.get(num,0) + 1
        # for num in nums2:
        #     if hashmap.get(num):#能get到内容时，才加入res
        #             res.append(num)
        #             hashmap[num] -= 1
        # return res
        # 假如两个数组排好序，如何优化你的算法
        # 时间复杂度O(NlogN+MlogM),空间复杂度O(min(M,N))
        # 如果一个长度很短一个长度很小，采用法2好，查询开销小
        # 若内存有限，法1好，只涉及到查询，而不用在内存中排序
        nums1.sort()
        nums2.sort()
        res, p1, p2 = [], 0, 0
        size1, size2 = len(nums1), len(nums2)
        while p1 < size1 and p2 < size2:
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1, p2 = p1 + 1, p2 + 1
            elif nums1[p1] > nums2[p2]:
                    p2 = p2 + 1
            else:
                p1 = p1 + 1
        return res
# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [1,2,2,1]
nums2 = [2,2,2]
s = Solution()
res = s.intersect(nums1,nums2)
print(res)