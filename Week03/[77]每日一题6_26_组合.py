# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 10:02 PM

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtracing(first=1, tmp=[]):
            if len(tmp) == k:  #触发结束条件 如果当前元素 已经有k个，就将它加入res中
                res.append(tmp[:])
            for i in range(first, n + 1):  # 如果当前元素个数小于k，则加入cur中
                # 做选择
                tmp.append(i)
                backtracing(i + 1, tmp)  # 进入下一层决策
                tmp.pop()  # 撤销刚才的选择

        res = []
        backtracing()
        return res
