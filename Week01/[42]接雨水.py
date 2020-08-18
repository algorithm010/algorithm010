# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/18 4:27 PM
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        size = len(height)-1
        dp0 = [0] * (size + 1)
        dp1 = [0] * (size + 1)
        dp0[0] = height[0]
        dp1[size] = height[-1]
        for i in range(1,size):
            dp0[i] = max(dp0[i-1],height[i])
        for i in range(size-1,-1,-1):
            dp1[i] = max(dp1[i+1],height[i])
        res = 0
        for i in range(size):
            res += min(dp0[i],dp1[i]) - height[i]
        return res

class SolutionI:
    def trap(self, height: List[int]) -> int:
        # 这里的标准解法肯定是 单调栈
        # 什么情况下能够接到雨水，当前height比左小，也比右小
        # 也就是说 维护一个单调递减栈，遇到比栈顶元素小的，就入栈，遇到比栈顶元素大的，将栈顶元素出栈
        # 计算刚才出栈元素下标出能接的水量
        if not height: return 0
        size = len(height)-1
        stack = []
        area = 0
        for i in range(size+1):#[2,0,2]如果下标只遍历到1，就没有用到右边的2，输出是0
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack: break#栈中只有一个元素的话，左边比当前元素还要小，存不住水
                # 注意在计算高度的时候，top原本是有高度的
                h = min(height[i],height[stack[-1]])-height[top]
                w = i - stack[-1] -1
                area += h*w
            stack.append(i)
        return area

s = SolutionI()
nums = [2,0,2]
res = s.trap(nums)
print(res)