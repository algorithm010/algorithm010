# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/21 9:15 PM

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxs = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # num = int(num)
                    box = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxs[box][num] = boxs[box].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxs[box][num] > 1:
                        return False
        return True

        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxs = [set() for _ in range(9)]
        # for i in range(9):
        #     for j in range(9):
        #         box_index, num = i // 3 * 3 + j // 3, board[i][j]
        #         if num != '.':
        #             if num in rows[i] or num in cols[j] or num in boxs[box_index]:
        #                 return False
        #             else:
        #                 rows[i].add(num)
        #                 cols[j].add(num)
        #                 boxs[box_index].add(num)
        # return True