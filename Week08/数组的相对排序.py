# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/2 11:00 AM

from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 双指针，左指针向后找不在arr2中的元素，右指针向前找到在arr2中的元素，交换left++right
        hashmap = {}
        for i, num in enumerate(arr1):
            hashmap[num] = hashmap.get(num,0) + 1
        ind = 0
        for i in range(len(arr2)):
            cur = arr2[i]
            while hashmap.get(cur) > 0:
                arr1[ind] = cur
                hashmap[cur] -= 1
                ind += 1
        # 将不在arr2中的元素升序排列,如何保证升序？？？
        print(hashmap)
        tmp = []
        for key, val in hashmap.items():
            # if val > 0:
            while val > 0 :
                tmp.append(key)
                hashmap[key] -= 1
                val -= 1
        tmp.sort()
        print('tmp',tmp)
        return arr1[:ind] + tmp
        #
s = Solution()
# nums1 = [2,3,1,3,2,4,6,7,9,2,19]
# nums2 = [2,1,4,3,9,6]
# [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]
nums1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
nums2 = [2,42,38,0,43,21]
res = s.relativeSortArray(nums1,nums2)
print(res)