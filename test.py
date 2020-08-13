# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/11 8:20 PM


# def decode(stack):
#     val1 = stack.pop()
#     val2 = stack.pop()
#     ch = chr(int(val1+val2,16))
#     if ch == '%':
#         stack = decode(stack)
#     else:
#         stack.append(ch)
#     return stack
# def main():
#     N = int(input())
#     for i in range(N):
#         s = str(input())
#         stack = []
#         for c in s[::-1]:
#             if c != '%':#%%32F
#                 stack.append(c)
#             else:
#                 stack = decode(stack)
#         print("".join(stack[::-1]))
# main()
# class Solution:
#     def minCost(self,x,a,b):
#         size = int((x+251)/500)#减少开辟的内存空间
#         dp = [0]*(size+1)
#         for i in range(1,3):
#             dp[i] = dp[i-1] + a
#         print(dp)
#         for i in range(3, size+1):
#             dp[i] = min(dp[i-3]+b, dp[i-1]+a)
#         return dp
# s = Solution()
# res = s.minCost(4999,5,10)
# print(res)
# def min_cost(x,a,b):
#     if x == 0: return 0
#     size = int((x+251)/500)
#     dp = [0]*(size+1)
#     for i in range(1,3):
#         dp[i] = dp[i-1] + a
#     for i in range(1,size+1):
#         dp[i] = min(dp[i-1]+a, dp[i-3]+b)
#     return dp[-1]

# def min_cost(x,a,b):
#     if 3*a <= b:
#         return x//500 * a#全部买小瓶的
#     else:#买1500ml均价更低
#         #先确定大瓶数量、在确定小瓶数量
#         m = x // 1500 + 1 if x % 1500 != 0 else x // 1500
#         # 1. 全买大瓶
#         cost1 = m * b
#         # 2. 尽可能买大瓶，剩下买小的
#         x = x - 1500 * (m - 1)
#         n = x // 500 + 1 if x % 500 != 0 else x // 500
#         cost2 = (m - 1) * b + n * a
#         return min(cost1, cost2)
# while True:
#     try:
#         N = int(input())
#         for i in range(N):
#             [x,a,b] = list(map(int,str(input()).split()))
#             res = min_cost(x,a,b)
#             print(res)
#     except:
#         break


# def cost(x, a, b):
#     if 3 * a < b:
#         n = x // 500 + 1 if x % 500 != 0 else x // 500
#         return n * a
#     else:
#         m = x // 1500 + 1 if x % 1500 != 0 else x // 1500
#         cost1 = m * b
#         x = x - 1500 * (m - 1)
#         n = x // 500 + 1 if x % 500 != 0 else x // 500
#         cost2 = (m - 1) * b + n * a
#         return min(cost1, cost2)
#
# while True:
#     try:
#         n = int(input())
#         for i in range(n):
#             [x, a, b] = list(map(int, input().split()))
#             print(cost(x, a, b))
#     except:
#         break
s= input().split(',')
print(s)
# a,b = list(map(int,[s1[1:-2],s2[:-2]]))
# print(a,b)