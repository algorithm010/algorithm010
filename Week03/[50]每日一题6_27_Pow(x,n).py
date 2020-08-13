# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/27 10:45 AM

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0: return 1
        # if n == 1: return x
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # return self.myPow(x*x,n//2) if n%2==0 else x*self.myPow(x,n-1)
        flag = 1
        if n < 0: flag = 0
        n, res = abs(n), 1
        while n:
            if n & 1:  # 奇数时
                res = res * x
            x = x * x
            n = n >> 1
        return res if flag else 1 / res

s = Solution()
res = s.myPow(2,4)
print(res)
