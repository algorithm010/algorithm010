# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/20 11:03 PM

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
#  说明：本题中，我们将空字符串定义为有效的回文串。
#
#  示例 1:
#
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
#  示例 2:
#
#  输入: "race a car"
# 输出: false
#
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #1. 翻转字符串 看是否相同 击败81%
        # tmp = "".join(ch.lower() for ch in s if ch.isalnum())
        # return tmp == tmp[::-1]
        #2.双指针 击败61%
        tmp = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(tmp)
        left, right = 0, n - 1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left, right = left + 1, right - 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
