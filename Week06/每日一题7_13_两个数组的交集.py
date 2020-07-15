# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/13 11:59 PM

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1.暴力解法 时间复杂度O(M*N),空间复杂度O(1)
        # res = [num for num in nums1 if num in nums2]
        # return set(res)
        # 2.hashmap 时间复杂度O(M+N),空间复杂度O(min(M,N))
        # hashmap, res = {}, []
        # for num in nums1:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        # for num in nums2:
        #     if hashmap.get(num):  # 能get到内容时，才加入res
        #         res.append(num)
        #         hashmap[num] -= 1
        # return set(res)
        # 3.奇技淫巧 时间复杂度应该是O(M+N),空间复杂度O(M+N)
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 ^ set2)
