# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/11 3:55 PM

# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre,head = head,tmp
        return pre

# leetcode submit region end(Prohibit modification and deletion)
