# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/16 10:54 PM

class Solution(object):
    def levelTraversal(self,root):
        # if root is None:
        #     return False
        # stack1, stack2 = [root], []
        # while stack1:  # 找出后序遍历的逆序，存放在 stack2中
        #     node = stack1.pop(0)#抛出第一个元素
        #     if node.left:
        #         stack1.append(node.left)
        #     if node.right:
        #         stack1.append(node.right)
        #     stack2.append(node.val)
        # return stack2#这里是层序遍历就不用反转了

        if not root: return []
        res, depth = [], 0
        self.dfs(root, res, depth)
        return res

    def dfs(self, root, res, depth):
        if not root: return
        if len(res) == depth: res.append([])  # 每当进入到一个新的depth，就创建一个[]
        res[depth].append(root.val)
        if root.left:
            self.dfs(root.left, res, depth + 1)
        if root.right:
            self.dfs(root.right, res, depth + 1)

