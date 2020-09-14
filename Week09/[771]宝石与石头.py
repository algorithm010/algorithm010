# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/5 12:14 AM


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 暴力法
        # count = 0
        # for ch in J:
        #     count += S.count(ch)
        # return count
        # hash表记录宝石 遍历待查字符串 这种题hash表解法一定不能忘！！！！！！！！！
        hashmap = set()
        count = 0
        for ch in J:
            hashmap.add(ch)
        for ch in S:
            if ch in hashmap:
                count += 1
        return count