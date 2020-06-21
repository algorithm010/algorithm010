# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/21 4:23 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
class Solution:
    def __init__(self):
        self.maxpath_sum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxGain(root)
        return self.maxpath_sum

    def maxGain(self,node):
        if not node: return 0
        left_gain = max(self.maxGain(node.left),0)#将空值、负值过滤掉了
        right_gain = max(self.maxGain(node.right),0)
        path_sum = node.val + left_gain + right_gain #左根右
        self.maxpath_sum = max(path_sum, self.maxpath_sum)#更新self.maxpath_sum，过滤负值
        return node.val + max(left_gain, right_gain)#返回此节点的最大贡献值，方便上层节点计算



