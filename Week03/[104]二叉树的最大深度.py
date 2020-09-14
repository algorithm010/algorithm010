# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/23 7:58 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #1.递归 击败50%
        # if root is None: return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        #2.迭代 击败77% BFS
        if root is None: return 0
        stack = [(1, root)]#栈中记录当前节点和此时的高度
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)#记录当前节点的高度
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth

