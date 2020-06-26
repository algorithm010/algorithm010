# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 5:29 PM

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, pre: List[int], inorder: List[int]) -> TreeNode:
        if not pre or not inorder:
            return None
        root = TreeNode(pre[0])
        index = inorder.index(root.val)#记录root在中序序列中的位置
        root.left = self.buildTree(pre[1:index+1],inorder[:index])
        root.right = self.buildTree(pre[index+1:],inorder[index+1:])
        return root