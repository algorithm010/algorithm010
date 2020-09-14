# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/13 12:08 AM
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
    #击败92%
    def push(self, x: int) -> None:
        self.stack.append(x)
        #如果当前元素比最小栈中的元素小，则将此元素放入最小栈中
        #如果当前最小栈为空，将此元素放入最小栈中
        if not self.min_stack :
            self.min_stack.append(x)
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            return self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
