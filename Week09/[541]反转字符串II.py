# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 10:27 AM


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #每隔2k个元素就将前k个元素逆序存到res中
        a = list(s)
        for i in range(0, len(a), 2*k):#将步长设置为2k即可
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)