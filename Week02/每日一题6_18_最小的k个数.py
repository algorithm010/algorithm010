# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/17 11:06 PM

from typing import List
import heapq
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         #暴力破解 击败64%
#         arr.sort()
#         return arr[:k]
# #
# #         #击败59%
#         if k == 0:
#             return []
#         heap = [-x for x in arr[:k]]  # 只用维护一个大小为k的小根堆
#         heapq.heapify(heap)  # 这k个元素一定满足三角顶最小的原则
#         for i in range(k, len(arr)):
#             if -heap[0] > arr[i]:
#                 heapq.heappop(heap)  # 如果堆中的元素大于入堆元素，则将原堆顶元素出堆
#                 heapq.heappush(heap, -arr[i])  # 将这个元素放入小根堆中，heappop中调用了siftup调整了堆
#         res = [-x for x in heap]
#         return res

class Solution:
    def partition(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and pivot <= nums[right]:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 快速排序法：
        size = len(arr)
        if size == 0 or k > size: return
        if size == 1 or size == k:
            return arr
        left, right = 0, size - 1
        while left <= right:  # 这里其实也相当于是二分法
            pivot = self.partition(arr, left, right)  # left, right, split_ind 都是原始 index
            if pivot == k:  # 在 split_ind 左边有 k 个元素，全部不大于 pivot
                break
            elif pivot > k:
                right = pivot - 1  # 不-1 会陷入死循环
            else:
                left = pivot + 1  # 不 +1 会陷入死循环
        return arr[:k]
s = Solution()
nums = [1, 4, 2, 5, 10, 3, -1]
res = s.getLeastNumbers(nums,2)
print(res)