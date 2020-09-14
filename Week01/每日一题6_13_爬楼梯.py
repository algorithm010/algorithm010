# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/13 11:59 AM

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1.无脑递归 未通过
        # if n==1: return 1
        # if n==2: return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        # 2.递归+备忘录,记录climbstairs(n)
        # 击败39%
        # mem = [0,1,2]
        # if n==1:return mem[1]
        # if n==2:return mem[2]
        # for i in range(3,n+1):
        #     mem.append(mem[i-1]+mem[i-2])
        # return mem[-1]
        # 3. 备忘录解法中相当于是存了1-n所有的结果，但是没有必要
        # 优化 击败83%
        a, b = 1, 2
        if n == 1: return 1
        if n == 2: return 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b



