# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/30 1:06 AM

# 您需要在二叉树的每一行中找到最大的值。
#
#  示例：
#
#
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# 输出: [1, 3, 9]
#
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 1. 思想比较简单 在二叉树的层序遍历的基础上 对每一列表求最大值后返回
        # 2. 当然也可以在遍历过程中记录每一层的最大值
        if not root: return []
        quene, res = [root], []
        while quene:
            cur_layer = []
            # layer_max = float('-inf')
            for _ in range(len(quene)):
                cur = quene.pop(0)
                if cur.left: quene.append(cur.left)
                if cur.right: quene.append(cur.right)
                # layer_max = max(layer_max, cur.val)
                cur_layer.append(cur.val)
            res.append(cur_layer)
            # res.append(layer_max)
        return [max(item) for item in res]
        # return res

# leetcode submit region end(Prohibit modification and deletion)
