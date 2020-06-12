# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/12 8:51 PM

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None

    def initList(self,data):
        self.head = ListNode(data[0])#链表头
        r,p = self.head,self.head
        for i in data[1:]:#循环创建链表
            node = ListNode(i)
            p.next = node
            p = p.next
        return r#返回头指针

    def printLinkList(self,head):
        if not head:
            return
        node = head
        while node != None:
            print(node.val,'->',end='')
            node = node.next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1) #dummy是用来返回最后的链表
        dummy.next = head
        pre = dummy#pre记录翻转过程每次翻转链表的前一个元素
        while head:
            tail = pre# last用以记录k个node的最后一个
            # 取出k个node
            for i in range(k):
                tail = tail.next
                if tail is None:#说明在取元素的时候没能够取到K个元素，返回的应该是头节点
                    return dummy.next
            next_head = tail.next#记录下个K组的首节点
            head,tail = self.reverseLinkList(head, tail)#这里传next_head,当做最后一个节点
            #将翻转后的链表接到原始链表上
            pre.next = head
            tail.next = next_head
            #调整此时的head和pre
            pre = tail
            head = next_head
        return dummy.next
    def reverseLinkList(self,head,tail):
        prev = tail.next
        tail_node = head#记录这K个node的第一个元素，最后将它作为尾元素返回 以连接到原始链表中
        while prev != tail:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return tail, tail_node
# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

ll = LinkList()
a = ll.initList([1,2,3,4,5,6])
# ll.printLinkList(a)
s = Solution()
res = s.reverseKGroup(a,2)
ll.printLinkList(res)