# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 1:16 AM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/house-robber-iii/solution/dfs-ni-neng-kan-dong-de-jie-shi-by-mqray/
class Solution:
    def rob(self, root: TreeNode) -> int:
        #要么就是偷左右孩子，要么就是偷根节点和直系孙子
        #dfs是求以该节点为根，在该点能拿到的最大值 对于这个节点，有拿和不拿两种
        def dfs(root):
            if not root: return 0, 0  # 偷，不偷
            left = dfs(root.left)
            right = dfs(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            # v2 = left[0] + right[0]
            v2 = max(left) + max(right)
            return v1, v2
        return max(dfs(root))