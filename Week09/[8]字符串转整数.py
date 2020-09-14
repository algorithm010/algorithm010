# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/5 12:37 AM

class Solution:
    def myAtoi(self, strs: str) -> int:
        res, sign = 0, 1
        strs = strs.strip()
        for i in range(len(strs)):
            ch = strs[i]
            if i == 0 and (ch == '-' or ch == '+'):
                if ch == '-': sign = -1
                if ch == '+': sign = 1
                continue  # 应对-123,是+-号之后就不用判断是否数字了
            if not ch.isdigit(): break  # 如果不是数字
            res = 10 * res + ord(ch) - ord('0')
        # 如果下越界 就返回-2**31 如果上越界返回2**31-1
        return max(-2 ** 31, -1 * res) if sign == -1 else min(2 ** 31 - 1, res)
