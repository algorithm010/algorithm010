# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/9 11:55 PM

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        最大的误区做题只做一遍
        优化：升维、空间换时间
        参考连接：https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down).
        """
        # 傻递归，时间复杂度是O(2^N)
        # if n == 1: return 1
        # if n == 2: return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # 击败39% 开辟数组像备忘录记录递归结果
        # if n == 1: return 1
        # tmp = [1, 2] + [0 for _ in range(n - 2)]  # 开辟额外数组空间
        # for i in range(2, n):
        #     tmp[i] = tmp[i - 1] + tmp[i - 2]
        # return tmp[-1]

        # 击败98% 优化 开辟数组过程
        # if n == 1: return 1
        # tmp = [0 for _ in range(n)]  # 开辟额外数组空间
        # tmp[0], tmp[1] = 1, 2
        # for i in range(2, n):
        #     tmp[i] = tmp[i - 1] + tmp[i - 2]
        # return tmp[-1]

        # 击败98.5% 只要一个额外的if判断
        if n == 1: return 1
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b



# leetcode submit region end(Prohibit modification and deletion)
