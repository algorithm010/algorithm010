# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/22 11:50 PM

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre_val = float('-inf')
    def isValidBST(self, root):
        """
        :type cur: TreeNode
        :rtype: bool
        """
        #依据是 二叉搜索树的中序遍历是有递增的 击败11%
        #recursive terminator
        # if root is None: return True
        # #current prpcess
        # #确定左子树是否符合排序二叉树，如果不满足，就返回False
        # if not self.isValidBST(root.left): return False
        # if root.val <= self.pre_val: return False#不满足左子树小于根节点
        # self.pre_val = root.val#记录上一个访问的节点的值
        # #访问右子树
        #
        # # drill down
        # return self.isValidBST(root.right)

        #中序遍历 迭代 击败73%
        stack, pre_val = [], float('-inf')
        cur = root
        while stack or cur is not None:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= pre_val: return False
            pre_val = cur.val
            cur = cur.right
        return True




# leetcode submit region end(Prohibit modification and deletion)
