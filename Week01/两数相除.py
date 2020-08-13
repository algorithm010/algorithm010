# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/29 1:43 AM

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #区分 两数的符号问题
        sign = (dividend>0) ^ (divisor>0) #异号为1
        dividend, divisor= abs(dividend), abs(divisor)
        res = 0
        while divisor <= dividend:
            tmp_divisor, count = divisor, 1 # 当不能被倍增后的整除时，将除数重置
            while tmp_divisor <= dividend:
                dividend -= tmp_divisor
                res += count
                count <<= 1
                tmp_divisor <<= 1
        res_value = -res if sign else res        # 给结果加上符号
        return max(min(res_value, 2**31-1), -2**31)

s = Solution()
res = s.divide(11,2)
print(res)


