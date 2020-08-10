# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/25 8:39 AM

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     res,max_length = '',0
    #     for i in range(len(s)):
    #         for j in range(i+1,len(s)+1):
    #             cur_string = s[i:j]
    #             if self.isPalidrome(cur_string) and len(cur_string)>max_length:
    #                 res = cur_string
    #                 max_length = max(max_length,len(res))
    #     return res
    #
    # def isPalidrome(self,cur_string):
    #     #判断是否回文字符
    #     left,right = 0,len(cur_string)-1
    #     while left<right:
    #         if cur_string[left]!=cur_string[right]:
    #             return False
    #         left,right = left+1,right-1
    #     return True

    # def longestPalindrome(self, s: str) -> str:
        # left, right, size = 0, 0, len(s)
        # def extend(left, right):
        #     while left >= 0 and right < size and s[left] == s[right]:
        #         left, right = left - 1, right + 1
        #     return left + 1, right - 1
        # for i in range(size):
        #     l1, r1 = extend(i, i)
        #     l2, r2 = extend(i, i + 1)
        #     if r1 - l1 > right - left:
        #         left, right = l1, r1
        #     if r2 - l2 > right - left:
        #         left, right = l2, r2
        # return s[left:right + 1]

    #首先 长度为0、1的字符串 它是回文串
    #长度=2，判断左右是否相同
    #对于strs[i,j]而言它是否是回文串 取决于它内缩2位的字符串是否是回文串同时还要判断其边界是否相同
    #动态规划的思想就是 每一次的状态都是可以由其他时刻的状态导出的
    #而通常我们在做题时，总会借助额外的空间，这个空间的维度与我们的状态有关，比如此时要记录i,j组合状态，就需要二维数组记录
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[False]*size for _ in range(size)]
        res = ''
        for l in range(size):
            for i in range(size):
                j = l + i
                if j >= size: break
                elif l == 0: dp[i][j] = True
                elif l == 1: dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i]==s[j])
                if l >= len(res) and dp[i][j]:#如果当前串是回文且长度增加
                    res = s[i:j+1]
        return res
        # size = len(s)
        # dp = [[False] * size for _ in range(size)]  # 为什么是一个二维数组
        # res = ""
        # # 枚举子串的长度 l+1
        # for L in range(size):
        #     # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
        #     for i in range(size):
        #         j = i + L
        #         if j >= len(s):
        #             break
        #         if L == 0:  # 如果当前字符长度为0
        #             dp[i][j] = True#i==j，为True
        #         elif L == 1:  # 如果当前字符长度为1
        #             dp[i][j] = (s[i] == s[j])
        #         else:  #
        #             dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
        #         if dp[i][j] and L + 1 > len(res):
        #             res = s[i:j + 1]
        # return res


s = Solution()
res = s.longestPalindrome("babad")
print(res)