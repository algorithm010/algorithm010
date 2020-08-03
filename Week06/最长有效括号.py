# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/30 2:09 AM

class Solution:
    def longestValidParentheses(self, strs: str) -> int:
        #先和面试官讨论清楚，最长有效括号是否是连续的
        pass
        #中心扩散？？？-->NO
        # 1.遍历可能的最大长度，再判断子串是否为有效子串 用栈实现O(N3)
        # 2.动态规划
        # dp = [0]*len(strs)#表示下标为i的有效括号长度
        # for i in range(len(strs)):
        #     if strs[i] == ')' and strs[i-dp[i-1]-1] =='(' and i-dp[i-1]-1>=0:#自身是否为有效括号
        #         dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]#自身+内有效括号+外有效括号
        # return max(dp)
        # 3.使用栈
        # stack = [-1]
        # length, max_length = 0, 0
        # # ")())())"
        # for i in range(len(strs)):# 小心这种情形 strs = "()(()"
        #     if strs[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if stack == []:
        #             stack.append(i)
        #         else:
        #             length = i - stack[-1]
        #             max_length = max(length, max_length)
        # return max_length
        #正反向遍历
        size,left,right,max_length = len(strs),0,0,0
        for i in range(size):
            if strs[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left*2)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0 #反序的时候清0
        for i in range(size-1, -1, -1):
            if strs[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left*2)
            elif left > right:
                left, right = 0, 0
        return max_length



s = Solution()
strs = "(()"
# strs = ")()())"
# strs = "()(())"
# strs = "()(()"
res = s.longestValidParentheses(strs)
print(res)