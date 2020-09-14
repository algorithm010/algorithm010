# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/19 8:07 PM

class Solution:
    def isUgly(self, num: int) -> bool:
        #如果一个数是丑数那肯定满足这种定义num = 2^i*3^j*5^k
        # for item in [2,3,5]:
        #     while num%item==0:#依次除尽2，3，5
        #         num = num/item
        # # return True if num==1 else False #击败50%
        # return num==1#击败87%
        if num == 0: return False
        while num % 5 == 0: num /= 5
        while num % 3 == 0: num /= 3
        while num % 2 == 0: num /= 2
        return num == 1#击败98%，省去了迭代的过程


s = Solution()
res = s.isUgly(7)
print(res)