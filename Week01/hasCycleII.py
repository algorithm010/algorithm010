# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/12 4:47 PM


# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  说明：不允许修改给定的链表。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
# 你是否可以不用额外空间解决此题？
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     # 1.hashtable beat 97%
    #     hashtable = {}
    #     while head:
    #         # if not in the hashtable
    #         if not hashtable.get(head):
    #             hashtable[head] = head
    #             # must move back the head pointer, so it can continue while loop
    #             head = head.next
    #         else:
    #             # if the node in hashtable, it must be the loop header
    #             return head
    #     # if walk here head==None, so we just return None
    #     return None
    # 击败28%
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return None
    #     intersect_node = self.interseet(head)
    #     if not intersect_node:  # if interset is None
    #         return None
    #     tmp = head
    #     while tmp != intersect_node:
    #         tmp, intersect_node = tmp.next, intersect_node.next
    #     return intersect_node
    #
    # def interseet(self, head: ListNode) -> ListNode:
    #     fast, slow = head, head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if slow == fast:
    #             return slow  # return the intersect
    #     return None
    #击败47%
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow, fast = slow.next, fast.next.next
    #         if slow == fast:
    #             break
    #     else:
    #         return None
    #     while head != slow:
    #         slow, head = slow.next, head.next
    #     return head
    #击败65%
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = finder = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                while slow != finder:
                    slow, finder = slow.next, finder.next
                return slow
        return None



# leetcode submit region end(Prohibit modification and deletion)
