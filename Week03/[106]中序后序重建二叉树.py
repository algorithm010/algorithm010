# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/12 11:17 PM


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder and not postorder: return
        val = postorder[-1]
        root_ind = inorder.index(val)
        root  = TreeNode(val)
        left = self.buildTree(inorder[:root_ind],postorder[:root_ind])
        right = self.buildTree(inorder[root_ind+1:],postorder[root_ind:-1])
        root.left = left
        root.right = right
        return root