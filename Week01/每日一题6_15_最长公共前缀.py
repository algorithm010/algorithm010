# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 5:40 PM

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#  示例 1:
#
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
#  示例 2:
#
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
#  说明:
#
#  所有输入只包含小写字母 a-z 。
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #击败59%
        # if not strs: return ''
        # min_size = min([len(x) for x in strs])  # 公共前缀最长只会这么长
        # for i in range(min_size, 0, -1):
        #     tmp = strs[0][:i]  # 当前待比较的公共前缀子串
        #     if all(s[:i] == tmp for s in strs):
        #         return tmp
        # return ''
        #击败78%
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.longestCommonPrefix(["dog","racecar","car"])
print(res)
