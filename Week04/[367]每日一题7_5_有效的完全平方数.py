# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/5 10:44 PM

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 二分法
        # left, right, res = 0, num//2+1, 0
        # while left <= right:
        #     mid = (left+right)//2
        #     if mid*mid < num:
        #         left = mid + 1
        #     elif mid*mid >num:
        #         right = mid - 1
        #     else:
        #         res = mid
        #         break
        # return res**2 == num
        # 拟牛顿法
        if num < 2: return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

