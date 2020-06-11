# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/11 8:23 PM

# 给定一个链表，判断链表中是否有环。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
#
#  你能用 O(1)（即，常量）内存解决此问题吗？
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 双指针解法 击败40%
        # if not head or not head.next:
        #     return False
        # fast, slow = head.next, head
        # while fast != slow:  # 相遇的时候退出此while返回True
        #     if fast == None or fast.next == None:
        #         return False
        #     fast = fast.next.next
        #     slow = slow.next
        # return True
        # hashtable 击败73%
        hashtable = {}
        if not head or not head.next:
            return False
        while head:  # 如果遍历完链表，则返回False
            if hashtable.get(head):
                return True
            else:  # 如果该节点没有出现过，则将其存入hashtable中
                hashtable[head] = True
                head = head.next
        return False
    # leetcode submit region end(Prohibit modification and deletion)
