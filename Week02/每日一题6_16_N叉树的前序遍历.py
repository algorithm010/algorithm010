# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/16 11:31 PM

# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #击败86%
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 击败95%
        if not root: return []
        res = []
        res.append(root.val)
        for child in root.children:
            res += self.preorderTraversal(child)
        return res

        #击败86%
    #     res = []
    #     if root:
    #         self.Npreorder(root, res)
    #     return res
    # def Npreorder(self, root, res):
    #     if root is None:
    #         return
    #     res.append(root.val)#先序遍历 先将值存入res，再依次访问子节点
    #     for child in root.children:
    #         self.Npreorder(child, res)

    #击败69%
    def traversal(self,root):
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for item in node.children[::-1]:
                stack.append(item)
        return res


# leetcode submit region end(Prohibit modification and deletion)
