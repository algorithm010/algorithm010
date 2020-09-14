# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 9:00 PM

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==0: return False#与面试官沟通边界
        # if n==1: return True
        # while n!=1:
        #     if n%2!=0: return False
        #     else: n = n//2
        # return True
        # 该数的二进制位有且仅有一个1
        if n==0: return False
        while n!=0:
            return (n&(n-1))==0 #打掉最后一个1看是否为0 以此检查是否只有一个1