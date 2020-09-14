# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/12 11:01 PM

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                    '7':'pqrs','8':'tuv','9':'wxyz'}
        # dfs
        # def backtrace(combinations,digits):#'23'
        #     if digits == '':
        #         res.append(combinations)
        #     else:
        #         for cur_str in hashmap[digits[0]]:#'abc'
        #             backtrace(combinations + cur_str,digits[1:])#'abc'中挑一个,'3'
        # res = []
        # # if digits:
        # backtrace('',digits)
        # return res
        # bfs
        if digits == '': return []
        combinations = ['']
        for digit in digits:
            combinations = [combination + cur for combination in combinations for cur in hashmap[digit]]
        return combinations

s = Solution()
res = s.letterCombinations('23')
print(res)