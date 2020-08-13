# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 12:49 AM

class Solution:
    def reverse(self, x: int) -> int:
        # 迭代反转数字
        flag = 0
        if x<0:
            x = abs(x)
            flag = 1
        res = 0
        while x>0:
            res = 10 * res + x % 10
            x = x//10
        res = -1 * res if flag==1 else res
        return res if -1*2**31<=res<=2**31-1 else 0
        #当然也可以使用栈来做，但要提前判断是否越界

s = Solution()
res = s.reverse(123)
print(res)