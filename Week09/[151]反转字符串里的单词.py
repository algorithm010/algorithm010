# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 10:27 AM


class Solution:
    def reverseWords(self, s: str) -> str:
        # #要注意到原字符串两边的空格以及 单词之间多余1的空格
        # tmp = s.split(' ')
        # #删除多余的空格
        # tmp = [] + [item for item in tmp if item!='']
        # # tmp = s.strip().split(' ')
        # tmp = list(reversed(tmp))
        # res = ' '.join(tmp )
        # return res
        return " ".join(reversed(s.split()))#split()不加参数会把结果中的' '删除