# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/22 9:30 PM
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    #1.递归的参数，递归的level
    # def _generate_parenthesis(self,level,max_level,strs):
    #     #recursive terminator
    #     if level>=max_level:
    #         print(strs)
    #         return
    #     #current process
    #     #drill down
    #     self._generate_parenthesis(level+1,max_level,strs+'(')
    #     self._generate_parenthesis(level+1,max_level,strs+')')
    # def generateParenthesis(self,n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     self._generate_parenthesis(0, 2*n, '')
    #击败43%
    def generateParenthesis(self, n):
        result = []
        self._generate_parenthesis(0, 0, n, '', result)
        return result

    def _generate_parenthesis(self, left, right, n, res, result):
        # recursive terminator
        if left == n and right == n:
            result.append(res)
            return
        # current process
        if left < n: self._generate_parenthesis(left + 1, right, n, res + '(', result)
        if left > right: self._generate_parenthesis(left, right + 1, n, res + ')', result)
    #击败82%，不需要传递五个变量
    def generateParenthesisII(self, n):

        def _generate_parenthesis(left, right, n, res):
            # recursive terminator
            if left == n and right == n:#触发结束条件
                result.append(res)
                return
            # current process #排除不合法的选择 做选择  进入下一层决策树
            if left < n: _generate_parenthesis(left + 1, right, n, res + '(')
            if left > right: _generate_parenthesis(left, right + 1, n, res + ')')
            #取消选择
        result = []
        _generate_parenthesis(0, 0, n, '')
        return result

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.generateParenthesis(3)
print(res)


