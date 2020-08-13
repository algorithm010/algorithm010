# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/5 10:27 PM

class Solution:
    def mySqrt(self, x: int) -> int:
        #1.换底公式求解
        # if x == 0: return 0
        # res = int(math.exp(0.5 * math.log(x)))
        # return res + 1 if (res + 1) ** 2 <= x else res
        #2.二分法
        # left, right, = 0, x
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid ** 2 <= x:  # x的整数部分的平方<=x
        #         res, left = mid, mid + 1
        #     else:
        #         right = mid - 1
        # return res
        #3.牛顿法迭代求解
        if x == 0: return 0
        x0 = A = float(x)
        while True:
            x1 = (x0 + A/x0)//2
            if abs(x1-x0)<1e-6:
                break
            x0 = x1
        return int(x0)