# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/14 5:32 PM
from typing import List
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        #这种接法就是应该是贪心吧？？如果匹配过程中，该元素都与均值匹配，那么就替换
        #每次都是与期望的均值作比较
        arr.sort()
        size = len(arr)
        for i in range(size):
            average = target / (size-i)#
            if arr[i] <= average:#如果当前元素小于平均值，那么再下次匹配时，希望的平均值就应当大一些
                target = target - arr[i]
            else:#如果当前的元素大于average，那么这个值就是可以修改的
                return int(average+0.49)
        #如果遍历完之后还没有返回这个value，说明整个数组整体的值都偏小，导致没法匹配到average值
        # 这个时候就返回排序数组最后的元素
        return arr[-1]