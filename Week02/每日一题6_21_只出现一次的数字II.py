# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/21 11:31 AM
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dic = {}#击败87%
        # for num in nums:
        #     dic[num] = dic.get(num,0)+1
        # for key, value in dic.items():
        #     if value == 1:
        #         return key
        # x, y = 0, 0#击败74%
        # for z in nums:#num means input
        #     y = ~x & (y^z)
        #     x = ~y & (x^z)
        # return y
        x,y = 0,0#击败57%
        for z in nums:
            tmp = ~x&(y^z)
            x = (x&~y&~z)|(~x&y&z)
            y = tmp
        return y