# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/29 10:29 PM
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 由于题目限制了最后打印输出格式每一层节点放在[]中，所以需要对普通的层序遍历进行调整
    # 在while quene循环中加入一个cur_layer记录当前层的节点以确保每次都能将该层的元素加入
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # if not root: return []
        # quene,res = [root],[]
        # while quene:
        #     cur_layer = []
        #     for _ in range(len(quene)):
        #         cur = quene.pop(0)
        #         if cur.left: quene.append(cur.left)
        #         if cur.right: quene.append(cur.right)
        #         cur_layer.append(cur.val)
        #     res.append(cur_layer)
        # return res

        #如果用DFS做，当然也可以得到想要的结果，只是要注意的是，遍历过程中，需要记录该节点的深度
        # 以便将它加入到res对应下标的位置
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])#在开始遍历时，生成一个[]位置，4接收参数
        res[level].append(root.val)
        if root.left: self.dfs(root.left, level + 1, res)
        if root.right: self.dfs(root.right, level + 1, res)