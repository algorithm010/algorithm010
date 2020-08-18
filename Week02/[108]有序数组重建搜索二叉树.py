# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/18 11:37 AM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(left,right):
            if left>right: return None
            mid = left + ((right-left)>>1)
            root = TreeNode(nums[mid])
            root.left = buildTree(left,mid-1)
            root.right = buildTree(mid+1,right)
            return root
        return buildTree(0,len(nums)-1)