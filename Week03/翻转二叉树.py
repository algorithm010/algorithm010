# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/22 11:08 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursive terminator
        #击败70%
        # if root is None: return
        # # current process
        # left = self.invertTree(root.right)
        # right = self.invertTree(root.left)
        # root.left = left
        # root.right = right
        # # drill down
        # # reverse states
        # return root
        #非递归写法，深度优先遍历过程中，交换左右孩子，然后继续向下做同样的操作
        #类似层序遍历，用quene存储访问到的节点
        #击败87%
        if root is None: return None
        quene = [root]
        while quene:
            cur = quene.pop()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left is not None: quene.append(cur.left)
            if cur.right is not None: quene.append(cur.right)
        return root




