# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/7 10:11 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, num: int) -> bool:
        #层序遍历
        if not root: return False
        node_quene = deque([root])
        val_quene = deque([root.val])
        while node_quene:
            cur_node = node_quene.popleft()
            cur_val = val_quene.popleft()
            if not cur_node.left and not cur_node.right:
                if num == cur_val:
                    return True
                continue#如果已经是叶节点，但sum和target相同，无需执行后面的判断语句
            if cur_node.left:
                node_quene.append(cur_node.left)
                val_quene.append(cur_val + cur_node.left.val)
            if cur_node.right:
                node_quene.append(cur_node.right)
                val_quene.append(cur_val + cur_node.right.val)
        return False
    #DFS深度优先遍历 递归
    def hasPathSumI(self, root: TreeNode, num: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return root.val == num
        return self.hasPathSumI(root.left, num - root.val) or self.hasPathSumI(root.right, num - root.val)
