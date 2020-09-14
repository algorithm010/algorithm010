# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/19 12:33 AM

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 1、2、3、5、4、6、8、9、10
        if n==0:
            return 0
        res = [1]*n
        p2,p3,p5 = 0,0,0#指向三个队列的指针
        for i in range(1,n):
            res[i] = min(res[p2]*2,res[p3]*3,res[p5]*5)
            if res[i] == res[p2]*2: p2 = p2+1
            if res[i] == res[p3]*3: p3 = p3+1
            if res[i] == res[p5]*5: p5 = p5+1
        return res[-1]