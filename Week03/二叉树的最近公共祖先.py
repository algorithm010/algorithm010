# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 1:11 PM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #1.递归 分析出找到最近公共祖先节点的情形，如果p，q由同一祖先节点 则p、q要么位于某棵树的左右子树
    #要么在同一棵树上，在同一棵树上又有 p或q为根 另外存在p或q在其左右子树中
    res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root,p,q)
        return self.res

    def dfs(self,root,p,q):
        # recursive terminator
        if root is None: return False
        #current process
        #drill down
        root_left = self.dfs(root.left,q,p)#判断这颗树的子树中是否含有q节点或者q节点
        root_right = self.dfs(root.right,p,q)
        #要判断p、q的最近公共祖先，我们从根节点开始寻找，查探root的左子树和右子树是否包含q节点或p节点，此时最近公共最先就是root；另外的，如果p或q为子树根节点，且p或q处在这棵子树下面，则最进公共祖先就是p或q节点
        if root_left and root_right or ((root.val==p.val or root.val==q.val) and(root_left or root_right) ):#对于5，1这种情况，这是后就要返回p为true给上层递归
            self.res = root#那么就返回当前树的根节点
        #reverse states
        return root_left or root_right or(root.val==p.val or root.val==q.val)

#2.记录父节点
class SolutionI:
    # ，然后我们就可以利用节点的父节点信息从p结点开始不断往上跳，并记录已经访问过的节点，再从q节点开始不断往上跳，如果碰到已经访问过的节点，那么这个节点就是我们要找的最近公共祖先。
    all_parents = {}
    p_parents = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.all_parents[root.val] = None
        self.dfs(root)  # 用哈希表存储所有节点的父节点
        # 在all_parents找p的根节点，并且记录找到的父节点
        while p != None:
            self.p_parents[p.val] = True
            p = self.all_parents.get(p.val)
        while q != None:  # 因为p、q是必有公共父节点的，所以一定能在p_parents里面找到父节点
            if self.p_parents.get(q.val):  # 如果如果在p的parent中找到
                return q
            q = self.all_parents.get(q.val)  # 如果没找到，说明q可能还要向上一层才能找到
        return None

    def dfs(self, root):  # 从root开始遍历子节点 记录子节点值作为key，值为root节点
        if root.left is not None:
            self.all_parents[root.left.val] = root
            self.dfs(root.left)
        if root.right is not None:
            self.all_parents[root.right.val] = root
        self.dfs(root.right)
