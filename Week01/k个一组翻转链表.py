# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/12 6:33 PM

# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
#  k 是一个正整数，它的值小于或等于链表的长度。
#
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
#  示例：
#
#  给你这个链表：1->2->3->4->5
#
#  当 k = 2 时，应当返回: 2->1->4->3->5
#
#  当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
#  说明：
#
#
#  你的算法只能使用常数的额外空间。
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)#dummy是用来返回最后的链表
        dummy.next = head
        pre = dummy#pre记录翻转过程每次翻转链表的前一个元素

        while head:
            tail = pre# last用以记录k个node的最后一个
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next#说明在取元素的时候没能够取到K个元素，返回的应该是头节点
            next_head = tail.next#记录下个K组的首节点
            head, tail = self.reverseList(head, tail)
            # 将翻转后的链表接到原始链表上
            pre.next = head
            tail.next = next_head
            # 调整此时的head和pre
            head = next_head
            pre = tail
        return dummy.next

    # 记录这K个node的第一个元素，最后将它作为尾元素返回 以连接到原始链表中
    def reverseList(self, head, tail):
        prev = tail.next
        tail_node = head
        while prev != tail:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return tail, tail_node
# leetcode submit region end(Prohibit modification and deletion)
