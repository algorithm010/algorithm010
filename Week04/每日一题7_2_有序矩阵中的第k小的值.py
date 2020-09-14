# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/2 7:25 PM
import heapq
from typing import  List
class Solution:
    #优秀的解释 时间复杂度是 O(KlogN)空间复杂度O(N)
    # https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/shi-yong-dui-heapde-si-lu-xiang-jie-ling-fu-python/
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)
        pq = [(matrix[i][0],i,0) for i in range(size)]# 维护一个最小元素队列 (i,0) means location
        heapq.heapify(pq)
        for i in range(k-1):#第k次pop的元素直接返回
            num, row, col = heapq.heappop(pq)
            if col != size - 1:
                heapq.heappush(pq,(matrix[row][col+1],row,col+1))#如果某行没有全部删除，将当前值右边的元素如堆
        # now time = k
        return heapq.heappop(pq)[0]

    def kthSmallestI(self, matrix: List[List[int]], k: int) -> int:
        # 1.暴力法 时间复杂度O(N^2) 空间复杂度为O(N^2)
        tmp = [x for item in matrix for x in item]
        tmp.sort()
        return tmp[-(len(tmp) - k + 1)]

    def kthSmallestII(self, matrix: List[List[int]], k: int) -> int:
        #双指针 时间复杂度O(Nlog(max-min))
        # n次双指针，每次判断矩阵左侧小于num的数的个数，大于k个则右指针已动到mid
        rows, cols = len(matrix), len(matrix[0])
        def check(num):
            i, j, count = rows - 1, 0, 0
            while i >= 0 and j < cols:
                if matrix[i][j] <= num:
                    count = count + i + 1  # 一竖行都小于
                    j = j + 1
                else:  # 如果大于num，这一层没有比num小的了
                    i = i - 1
            return count >= k

        left_up, right_down = matrix[0][0], matrix[rows - 1][cols - 1]
        while left_up < right_down:
            mid = (left_up + right_down) // 2
            if check(mid):
                right_down = mid  # 左边有大于k个数，那么第k小的数肯定在左边
            else:  # 左边没有k个数
                left_up = mid + 1
        return left_up


