# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/16 9:37 PM

class Solution(object):
    # def postorderTraversal(self,root):
    #     res = []
    #     if root is not None:
    #         self.postorder(root, res)
    #     return res
    # def postorder(self,root,res):
    #     if root.left is not None:
    #         self.postorder(root.left)
    #     if root is not None:
    #         res.append(root.val)
    #     if root.right is not None:
    #         self.postorder(root.right)
    def postorderTraversal(self, root):
        #用两个栈实现后序遍历的非递归实现
        if root is None:
            return False
        stack1, stack2 = [root], []
        while stack1:  # 找出后序遍历的逆序，存放在 stack2中
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2[::-1]








