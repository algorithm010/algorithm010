# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 8:40 PM

# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution(object):
    #1.递归实现 击败 67%
    # def inorderTraversal(self, root):
    #     """
    #     #中序遍历 左根右
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if root:
    #         self.inorder(root, res)
    #     return res
    # def inorder(self, root, res):
    #     if root.left:
    #         self.inorder(root.left, res)
    #     if root:
    #         res.append(root.val)
    #     if root.right:
    #         self.inorder(root.right, res)
    # 击败21%
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res




    # leetcode submit region end(Prohibit modification and deletion)
