# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/21 10:24 AM

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #1.hash表记录出现次数，以num为key，以出现次数为value 击败42%
        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num,0)+1
        # for key, value in dic.items():
        #     if value == 1:
        #         return key
        #位运算，击败91%
        # 由于每个元素都出现了两次，根据异或运算可以消去这两个元素
        #最后保留的就是带求值key和初始值1的异或
        res = 1
        for num in nums:
            res ^= num
        # print(res)
        return res ^ 1


s = Solution()
res = s.singleNumber([4,1,2,1,2])
print(res)