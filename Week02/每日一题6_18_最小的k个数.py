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
            elif pivot > k:#如果左边还有大于k个数，继续在左边找
                right = pivot - 1  # 不-1 会陷入死循环
            else:
                left = pivot + 1  # 不 +1 会陷入死循环
        return arr[:k]



import heapq

class SolutionII:
    #如果 是要求最小的k个数，那么应该是维护一个大小为k的大根堆，如果元素值小于堆顶元素，
    # 将此元素放到数组末尾，进行heapify，那么每次就相当于将原始数组中的大数全部推出，只留下最后k个，那他就是最小值
    # 判断当前元素是否小于堆顶元素，如果小，就入堆

    # 同理 如果要求最大的k个数，那么就需要维护小根堆，一致删除较小的元素，直到元素组只剩k个值，就是最大的k个数
    # 但是由于python中的heapq是小根堆，所以我们在维护堆之前先将符号调换一下
    # 小根堆 如果当前值大于堆顶元素 才能入堆
    def getLeastNumbers(self, nums, k):
        if k == 0: return []
        my_heap = [-x for x in nums[:k]]#维护大小为k的小顶堆
        heapq.heapify(my_heap)
        for i in range(k,len(nums)):
            if -nums[i] > my_heap[0]:#小根堆最后留下的是最大的k个值，所以只有大于堆顶才能进
                heapq.heappop(my_heap)
                heapq.heappush(my_heap,-nums[i])
        res = [-x for x in my_heap]
        return res

        # heapq.heapify(my_heap)#维护大小为k的小根堆
        # for i in range(k,len(nums)):
        #     if nums[i] < my_heap[-1]:#如果比栈顶元素小，将当前栈顶元素






s = SolutionII()
# nums = [1, 4, 2, 5, 10, 3, -1]
nums = [0,0,1,2,4,2,2,3,1,4]
res = s.getLeastNumbers(nums,8)
print(res)