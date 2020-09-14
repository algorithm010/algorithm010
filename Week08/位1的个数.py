# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 8:59 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 笨方法
        # tmp = bin(n)[2:]
        # count = 0
        # for i in range(len(tmp)):
        #     if tmp[i] == '1':
        #         count += 1
        # return count
        # count = 0
        # while n!=0:
        #     if n & 1 == 1:#判断最低位是否为1
        #         count += 1
        #     n = n >>1
        # return count
        count = 0
        while n!=0:
            n = n & (n-1)#清除最低位的1
            count += 1
        return count