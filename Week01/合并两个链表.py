# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 5:37 PM

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
#  示例1：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  限制：
#
#  0 <= 链表长度 <= 1000
#
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
#  Related Topics 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:  # 如果l1为空，直接返回l2
            return l2
        if not l2:  # 如果l2为空，直接返回l1
            return l1
        rhead = ListNode(None)  # 用来返回最后的结果的节点
        pre = rhead  # 用来添加比较过的节点
        while l1 and l2:  # 循环直到某链表没有值结束,刚开始这里写的是l1.next and l2.next 返回的结果是[1,1,2,4]
            if l1.val <= l2.val:
                tmp, l1 = l1, l1.next  #
                pre.next = tmp
                pre = tmp
            else:
                tmp, l2 = l2, l2.next
                pre.next = tmp
                pre = tmp
        if not l1:
            pre.next = l2
        if not l2:
            pre.next = l1
        return rhead.next
# leetcode submit region end(Prohibit modification and deletion)
