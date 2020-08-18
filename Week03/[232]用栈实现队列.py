# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/16 2:03 PM


class MyQueue:
    #用栈实现队列，最要考虑的就是抛出的时候该怎么做
    # 抛出首先检查栈2是否为空，如果不为空，就抛出栈2顶元素
    # 如果为空 就将栈1中的元素全部转移到栈2中，抛出栈2顶元素
    # 如果栈1也为空，就抛出 异常
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:#如果栈2中有元素，直接从栈2中抛出
            return self.stack2.pop()
        while self.stack1:#如果栈2中没有元素了，那就将栈1中的元素全部转移到栈2
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()