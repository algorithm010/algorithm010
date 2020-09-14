# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/6 12:25 AM

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        raws = len(matrix)
        cols = len(matrix[0])
        if raws == 0 or cols == 0:
            return False
        raw, col = 0, cols - 1
        # 方法一:从右上角开始搜索,时间复杂度为O(N+M))
        while raw < raws and col >=0:
            if matrix[raw][col] == target:
                return True
            elif matrix[raw][col] < target:
                raw += 1
            else:
                col -= 1
        return False
    # 方法二:二分查找
    def searchMatrixI(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        raws = len(matrix)
        if len(matrix[0]) == 0: return False
        cols = len(matrix[0])
        if not matrix: return False
        raws, cols = len(matrix), len(matrix[0])
        up, bottom = 0, raws - 1
        while up <= bottom:
            row = (up + bottom) >> 1
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] < target:
                up = row + 1
            else:
                bottom = row - 1
        raw = bottom
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) >> 1
            if matrix[raw][mid] == target:
                return True
            elif matrix[raw][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    #代码简化版 二分查找
    def searchMatrixII(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]#刚好可以得到行列号
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False
