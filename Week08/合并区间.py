# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/2 11:55 AM

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #按区间左端点值进行排序，那么能合并的区间必然相连
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:#区间右值小于起始值
                res.append(interval)
            else:#否则更新右值
                res[-1][1] = max(res[-1][1],interval[1])
            print(res)
        return res


s = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
res = s.merge(nums)
print(res)