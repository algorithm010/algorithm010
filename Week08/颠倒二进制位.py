# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 9:13 PM

class Solution:
    def reverseBits(self, n: int) -> int:
        # 脱裤子放屁
        # tmp = bin(n)[2:].zfill(32)
        # return int(tmp[::-1],2)
        # 逐位颠倒
        res, bits = 0, 31
        while n!=0:
            res += (n&1)<<bits
            n = n>>1
            bits -= 1
        return res
