# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/3 12:25 AM

from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills: return True
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0: return False
                five, ten = five - 1, ten + 1
            else:#change 15
                if five and ten:
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five = five - 3
                else:
                    return False
        return True
