# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/28 11:57 PM

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    # 分治算法，每次归并链各个链表01-0,23-2 步长倍增
    # 下次就归并02-0 46-4
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        size = len(lists)
        step = 1
        while step < size:
            for i in range(0,size-step,step*2):
                lists[i] = self.merge2list(lists[i],lists[i+step])
            step = step * 2
        return lists[0]

    def merge2list(self,l1,l2):
        pre = head = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if not l1:
            head.next = l2
        if not l2:
            head.next = l1
        return pre.next
from queue import PriorityQueue
class SolutionII:
    # 使用优先级队列 省去每次链表头结点的大小比较
    # 这段代码在python3中不过，应为优先级队列
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre = head = ListNode(-1)
        pq = PriorityQueue()
        for l in lists:
            if l:
                pq.put((l.val,l))#优先级在前
        while pq:
            val, node = pq.get()
            head.next = node
            node = node.next
            head = head.next
            if node:
                pq.put((node.val,node))#优先级队列中加入一个
        return pre.next


