# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/25 1:42 PM
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        # 手写一个二叉树的层寻遍历
        if not root: return []
        dquene, res = [root], ''
        while dquene:
            cur = dquene.pop(0)  # 使用了双端队列
            if cur != None:
                res += str(cur.val) + ','
                dquene.append(cur.left)
                dquene.append(cur.right)
            else:
                res += '#,'
        return res

    def deserialize(self, data):
        if not data: return None
        data = data.split(',')
        root = TreeNode(data.pop(0))
        dquene = [root]
        while dquene:
            cur = dquene.pop(0)
            if data:
                cur_left = data.pop(0)
                if cur_left != '#':  # 反序列化时，如果节点值为#就不处理
                    cur.left = TreeNode(cur_left)
                    dquene.append(cur.left)
                # if data:
                cur_right = data.pop(0)
                if cur_right != '#':
                    cur.right = TreeNode(cur_right)
                    dquene.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))