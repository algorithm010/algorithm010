# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/16 8:56 PM

# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution(object):
    # 递归方式，击败96%
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if root:
    #         self.preorder(root, res)
    #     return res
    #
    # def preorder(self, root, res):  # 前序遍历 根左右
    #     if root:
    #         res.append(root.val)
    #     if root.left:
    #         self.preorder(root.left, res)
    #     if root.right:
    #         self.preorder(root.right, res)
    #非递归方式 击败86%
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 前序遍历的迭代实现
        if root is None: return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur is not None:
                res.append(cur.val)
                # 考虑到入栈的顺序，所以先右后左
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
        return res

# leetcode submit region end(Prohibit modification and deletion)
