# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 11:21 PM

# hashmap+double-linklist

class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        node = self.dic[key]
        self.delete(node)#访问过后要将它放到链表头部
        self.insert(node)
        return node.val

    def insert(self,node):
        node.next, node.prev = self.head.next, self.head
        temp = self.head.next
        self.head.next = node
        temp.prev = node

    def delete(self,node):
        node.prev.next, node.next.prev = node.next, node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.dic:#如果相同key值出现过，更新dic和链表
            node = self.dic[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            return
        if len(self.dic) == self.capacity:
            node=self.tail.prev#删除第一个元素
            self.delete(node)
            del self.dic[node.key]
            self.capacity -= 1
        node = ListNode(key,value)#将此元素加入到第一个元素
        self.dic[key] = node
        self.insert(node)
        self.capacity += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def put(self, key, value):
        # 先判断要放进去的元素是否在hashmap里面
        if key not in self.dic:  # 如果不在里面
            if self.capacity != 0:  # 如果不在里面且还有额外的空间，就往里加
                self.insert(key, value)
            else:  # 没有额外的空间了，就应当删除双向链表中的最后一个元素
                last = self.tail.pre
                self.delete(last)
                self.insert(key, value)
        else:  # 如果在里面
            # 应当先删除这个元素/更新
            cur = self.dic[key]
            self.delete(cur)  # 删除这一个
            self.insert(key, value)

    def get(self, key):
        if key not in self.dic:
            return -1
        else:
            # 将该元素放到head之后
            cur = self.dic[key]
            value = cur.val
            self.delete(cur)
            self.insert(key, value)
            return value

    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.dic[node.key]
        self.capacity += 1

    def insert(self, key, value):
        cur = ListNode(key, value)
        cur.next = self.head.next
        cur.pre = self.head
        tmp = self.head.next
        tmp.pre = cur
        self.head.next = cur
        self.capacity -= 1
        self.dic[key] = cur