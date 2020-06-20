# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/20 10:11 PM

# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#  说明:
#
#
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
#  示例 1:
#
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
#  示例 2:
#
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
#  示例 3:
#
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#  示例 4:
#
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
#  示例 5:
#
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#  Related Topics 字符串 动态规划 回溯算法

from functools import lru_cache
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    #1.将复杂问题进行拆解 递归 但是明显是超出时间限制的，时间复杂度是O(3^N)
    # s="aaaaaaaaaaaaab"
    # pattern="a*a*a*a*a*a*a*a*a*a*c" 但是python中可以使用@lru_cache装饰器优化递归过程
    @lru_cache
    def isMatch(self, s: str, pattern: str) -> bool:
        # # 特殊情况处理
        # if len(s) == 0 and len(pattern) == 0: return True
        # if len(s) > 0 and len(pattern) == 0: return False
        # # 如果pattern形如 a*####，检查这个*能匹配几次
        # if len(pattern) > 1 and pattern[1] == '*':#击败80%
        #     # s和pattern首字母相同
        #     if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
        #         # s能和pattern匹配的情形
        #         # 1.*匹配0次，则需要递归的对s和pattern[2:]进行匹配
        #         # 2.*匹配1次，需要递归的对s[1:]和pattern[2:]进行匹配
        #         # 3.*匹配n次，需要递归的对s[1:]和pattern进行匹配
        #         return self.isMatch(s, pattern[2:]) or self.isMatch(s, pattern[2:]) or self.isMatch(s[1:], pattern)
        #     else:  # 如果首字母不相同，就相当于*匹配0次，继续匹配s和pettern[2:]
        #         return self.isMatch(s, pattern[2:])
        # # pattern以.开头
        # if len(s) > 0 and (pattern[0] == '.' or s[0] == pattern[0]):
        #     return self.isMatch(s[1:], pattern[1:])
        # return False
        #击败86%
        if not pattern: return not s
        match_first = bool(s) and (pattern[0] == s[0] or pattern[0] == '.')
        if len(pattern) > 1 and pattern[1] == '*':
            return (self.isMatch(s, pattern[2:]) or match_first and self.isMatch(s[1:], pattern))
        else:
            return match_first and self.isMatch(s[1:], pattern[1:])
# leetcode submit region end(Prohibit modification and deletion)
