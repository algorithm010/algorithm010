# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/19 8:41 PM
from typing import List
class Solution:
    # : List[int], k: int
    def topKFrequent(self, nums) -> List[int]:
        dic = {}
        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                dic[num] += 1
        res = sorted(dic.items(),key=lambda item:item[1])
        return res

nums = [1,1,1,2,2,3]
s = Solution()
res = s.topKFrequent(nums)
print(res)