# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/23 8:52 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #击败21%
        #recursive terminator
        #1.根节点为空 return 0
        #2. 左右节点为空 return 1
        #3.左节点或右节点为空 return 左/右+1
        #4.左右节点都不为空 return min(left,right)+1
        # if root is None: return 0
        # if root.left is None and root.right is None: return 1
        # left_height, right_height = self.minDepth(root.left),self.minDepth(root.right)
        # if root.left is None or root.right is None:  return left_height+right_height+1#有一个为0
        # #其余情况 返回较小值+1
        # return min(left_height,right_height)+1

        # 2.深度优先搜索

        # 3.广度优先搜索
        #借助双端队列 击败86%
        if not root: return 0
        quene = [(1, root)]
        while quene:
            #[3,9,20,null,null,15,7]
            depth, root = quene.pop(0)  # 保证从左往右看，如果是pop(0)，那么可能往右看的过程中返回了，而丢失了应有的最小值
            if not root.left and not root.right: return depth  # 如果此节点左右为空 返回当前depth
            if root.left: quene.append((depth + 1, root.left))
            if root.right: quene.append((depth + 1, root.right))