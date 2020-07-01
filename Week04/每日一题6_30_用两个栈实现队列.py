# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/30 7:14 PM

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
#
#
#  示例 1：
#
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
#
#  示例 2：
#
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#
#
#  提示：
#
#
#  1 <= values <= 10000
#  最多会对 appendTail、deleteHead 进行 10000 次调用
#
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue(object):

    def __init__(self):
        self.in_stack, self.out_stack = [],[]

    def appendTail(self, value):
        self.in_stack.append(value)

    def deleteHead(self):
        """
        删除的时候有几点要考虑，
        1.如果out_stack中有元素，说明是上一次删除没有删除完的，最优先删除
        2.如果out_stack中元素全部删除后，in_stack中没有元素，则无法删除返回-1
        3.如果in_stack中有元素，将其全部转移到out_stack中，返回pop()值
        """
        if self.out_stack: return self.out_stack.pop()
        if not self.in_stack: return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)
