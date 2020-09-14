# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/26 5:38 PM

# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#
#  示例1:
#
#
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
#
#
#  示例2:
#
#
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
#
#
#  提示：
#
#
#  链表长度在[0, 20000]范围内。
#  链表元素在[0, 20000]范围内。
#
#
#  进阶：
#
#  如果不得使用临时缓冲区，该怎么解决？
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        once = {head.val}
        pre = head
        while head.next:  # 如果有下一个节点
            cur = head.next
            if not cur.val in once:
                once.add(cur.val)
                head = head.next
            else:  # 如果这个元素已经出现，那就直接删除掉
                head.next = head.next.next
        return pre
# leetcode submit region end(Prohibit modification and deletion)
