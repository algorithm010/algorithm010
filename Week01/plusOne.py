# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/14 10:23 PM
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #击败99%
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0 #[9,9,9,9]的情况处理完再返回
        # digits.insert(0, 1)#这个击败89%
        # return digits #往第0个位置插入1
        return [1]+digits
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.plusOne([1,9])
print(res)
