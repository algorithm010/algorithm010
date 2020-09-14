# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/4 11:26 PM

class Solution:
    def toLowerCase(self, str: str) -> str:
        # return str.lower()
        # A 65 a 97 差32  '0'的ascii 为48
        # ord('x')-->ascii值
        # chr(ascii值)-->str
        res = ''
        for i in range(len(str)):
            if 65<= ord(str[i]) < 97:
                res += chr(ord(str[i])+32)
            else:
                res += str[i]
        return res