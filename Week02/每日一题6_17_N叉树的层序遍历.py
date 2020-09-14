# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/17 10:27 PM

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    def levelOrder(self,root):
        #击败55%
        if root is None: return []
        quene,res = [root],[]
        while quene:
        #将当前层的所有元素出队列，记录其值存入res中，由于输出格式的限制，要用tmp先存放
        #并且将其孩子全部记录在下一个quene中，这样保证了上层节点全部被加入到res中，而不会发生交替现象
            tmp, tmp_quene = [], []#这个tmp_quene是为了暂存下一层的所有节点
            for node in quene:
                tmp.append(node.val)
                for child in node.children:
                    tmp_quene.append(child)
            res.append(tmp)
            quene = tmp_quene
        return res