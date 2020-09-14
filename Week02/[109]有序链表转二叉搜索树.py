# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/18 11:13 AM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度O(nlogn),空间复杂度O(logn)
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 找到根节点，左右子树继续找根节点
        def findroot(left,right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildBST(left,right):
            if left == right: return None
            node = findroot(left,right)
            root = TreeNode(node.val)#产生空间开销
            root.left = buildBST(left,node)#注意这里是分治的过程，左右子树继续找根节点，
            root.right = buildBST(node.next,right)
            return root
        return buildBST(head,None)
