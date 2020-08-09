# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/7 10:47 PM


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val!=q.val: return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)