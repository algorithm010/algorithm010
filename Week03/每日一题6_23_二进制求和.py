# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/23 9:28 PM

# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
#  输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
#  示例 1:
#
#  输入: a = "11", b = "1"
# 输出: "100"
#
#  示例 2:
#
#  输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
#  提示：
#
#
#  每个字符串仅由字符 '0' 或 '1' 组成。
#  1 <= a.length, b.length <= 10^4
#  字符串如果不是 "0" ，就都不含前导零。
#
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #1.利用进制转换来做
        # return bin(int(a, 2)+int(b, 2))[2:]
        #2.如果不能使用加减乘除运算，则使用位运算
        x, y = int(a, 2), int(b, 2)
        while y:
            res = x ^ y #无进位相加结果
            carry = (x & y) << 1#计算x+y的进位
            x, y = res, carry
        return bin(x)[2:]
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
a, b = "1010", "1011"
res = s.addBinary(a, b)
print(res)