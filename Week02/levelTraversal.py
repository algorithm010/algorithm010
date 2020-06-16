# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/16 10:54 PM

class Solution(object):
    def levelTraversal(self,root):
        if root is None:
            return False
        stack1, stack2 = [root], []
        while stack1:  # 找出后序遍历的逆序，存放在 stack2中
            node = stack1.pop(0)#抛出第一个元素
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2#这里是层序遍历就不用反转了

