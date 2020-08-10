# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 2:25 AM


class Solution:
    def letterCasePermutation(self, strs: str) -> List[str]:
        #如果下一个字符时字母，则将已经生成的排列拷贝一份，将下一个字母转为大小写，加到排列后
        # 如果是数字，直接加到所有排列后
        # 时间复杂度是2^n*N
        res = ['']
        for i in range(len(strs)):
            if strs[i].isalpha():
                res = [item+case for item in res for case in [strs[i].lower(),strs[i].upper()]]
            elif strs[i].isdigit():
                res = [item+str(strs[i]) for item in res]
        return res