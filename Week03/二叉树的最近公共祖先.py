# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 1:11 PM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #1.递归 分析出找到最近公共祖先节点的情形，如果p，q由同一祖先节点 则p、q要么位于某棵树的左右子树
    #要么在同一棵树上，在同一棵树上又有 p或q为根 另外存在p或q在其左右子树中
    def lowestCommonAncestor(self, root, p, q):
        # dfs
        # if not root or p == root or q == root : return root
        # left = self.lowestCommonAncestor(root.left,p,q)#表示左子树是否包含p或q
        # right = self.lowestCommonAncestor(root.right,p,q)
        # if left and right: return root
        # return left if left else right
        # hash表解法
        hashmap = {root: None}

        def dfs(root):
            if root:
                if root.left: hashmap[root.left] = root
                if root.right: hashmap[root.right] = root
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        left, right = p, q  # 转化为找两个链表的相交节点
        while left != right:
            left = hashmap.get(left, q)
            right = hashmap.get(right, p)
        return left
