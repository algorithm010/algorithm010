# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/11 4:13 PM

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1. 迭代
        # preparing listnode
        # dummy node for return the list head
        # beat 9%
        # dummy = ListNode(-1)
        # dummy.next = head
        # pre = dummy
        #
        # while head and head.next:
        #     # prepare the two node
        #     first_node = head
        #     second_node = head.next
        #
        #     # swap the two node
        #     pre.next = second_node
        #     first_node.next = second_node.next
        #     second_node.next = first_node
        #
        #     # reset the pre and head point for next swap
        #     pre = first_node
        #     head = first_node.next
        # return dummy.next

        # 击败49%
        # dummy = prev = ListNode(0)
        # prev.next = head
        #
        # while prev.next and prev.next.next:
        #     a, b = prev.next, prev.next.next
        #     prev.next, a.next, b.next = b, b.next, a
        #     prev = a
        #
        # return dummy.next

        # trying recursive 击败6%
        # 递归无非是 地递归过程中的操作，以及每层递归要返回的
        # 1.
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next

        # 递归过程
        # 相邻元素倒置，以及外加一条向外连接的线
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node
# leetcode submit region end(Prohibit modification and deletion)
