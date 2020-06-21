# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/21 11:40 AM
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #击败64%
        # dic,res = {}, []
        # for num in nums:
        #     dic[num] = dic.get(num,0) + 1
        # for key,value in dic.items():
        #     if value == 1:
        #         res.append(key)
        # return res
        tmp = 0
        for num in nums:
            tmp ^= num
        # rightmost 1-bit diff between x and y
        diff = tmp & (-tmp)  # 这个找到第一位不相同的方式厉害
        x = 0
        for num in nums:
            if num & diff:  # 结果大于0执行，此位为1为一组，直接计算
                x ^= num
        return [x, tmp ^ x]  # tmp是两个数的异或值，一个值已经找到了

