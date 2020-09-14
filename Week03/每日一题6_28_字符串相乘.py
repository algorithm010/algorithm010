# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/28 7:21 PM

# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  示例 1:
#
#  输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#
#  输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#  说明：
#
#
#  num1 和 num2 的长度小于110。
#  num1 和 num2 只包含数字 0-9。
#  num1 和 num2 均不以零开头，除非是数字 0 本身。
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):  # 确定num1是较长的
            num1, num2 = num2, num1
        tmp,tail = 0,0
        for i in range(len(num1)):
            tail = tail + int(num1[i])*10**(len(num1)-i-1)
        for ind in range(len(num2)-1, -1, -1):#将较长的作为底数，这样int()转换的时候不会出错
            # tmp = tmp + int(num1) * 10 ** (len(num2) - ind - 1) * int(num2[ind])
            tmp = tmp + tail * 10 ** (len(num2) - ind - 1) * int(num2[ind])
        return str(tmp)

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
num1, num2 = '123', '456'
res = s.multiply(num1, num2)
print(res)