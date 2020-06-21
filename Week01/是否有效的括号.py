# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/12 11:22 PM

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #击败96%
        stack = []
        dic = {')':'(',']':'[','}':'{'}
        for item in s:
            if item not in dic:#如果是左括号，入栈
                stack.append(item)
            else:#如果是右括号
                top = stack.pop() if stack else '#'#判断是否与当前栈顶元素相匹配
                if top != item:#不匹配，则返回False
                    return False
        #如果刚开始是左括号，入栈后就结束了，明显是不匹配的，所以最终结果需要根据stack是否空来返回
        return not stack
    # leetcode submit region end(Prohibit modification and deletion)
