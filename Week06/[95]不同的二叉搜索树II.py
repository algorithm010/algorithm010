# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/6 1:25 AM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        def generate_trees(start,end):
            if start > end: return [None]
            trees = []
            for i in range(start, end+1):
                ltree = generate_trees(start,i-1)
                rtree = generate_trees(i+1,end)
                for lnode in ltree:
                    for rnode in rtree:
                        cur = TreeNode(i)
                        cur.left = lnode
                        cur.right = rnode
                        trees.append(cur)
            return trees
        return generate_trees(1,n) if n else []