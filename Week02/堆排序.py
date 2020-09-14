# # -*- coding:utf-8 -*-
# # Author : Ray
# # Data : 2020/6/18 7:06 PM
#
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# #  @Time    : 2019/12/2 18:25
# #  @Author  : mqray
# #  @File    : 选择排序之堆排序#
#
class HeapSort():
    '''
    时间复杂度为NlogN，logN为建立大根堆/小根堆的时间复杂度，
    heapify的时间复杂度是O(logN)的因为，最坏情况下，每一层都需要判断
    N为对已经构成的堆排序反向遍历的时间复杂度
    '''
    def heapify(self, nums, size, i):#heapify过程就是递归考量三角是否满足条件
        max_index = i
        left, right = 2*i+1,2*i+2
        if left < size and nums[left] > nums[max_index]:
            max_index = left
        if right < size and nums[right] > nums[max_index]:
            max_index = right
        if max_index != i:#存在交换的情形
            nums[i], nums[max_index] = nums[max_index], nums[i]
            self.heapify(nums, size, max_index)

    def heap_sort(self,nums):
        size = len(nums)
        for i in range(size//2-1,-1,-1):
            self.heapify(nums,size,i)

        for i in range(size-1,0,-1):#排序需要对整个堆进行调整
            nums[i], nums[0] = nums[0], nums[i]#交换末尾元素与堆顶元素
            self.heapify(nums,i,0)#交换之后，要确定这个堆是否合乎条件，进行堆化，
            #要注意到，每次堆化时，就已经把一个元素排好了，放在最末尾了，以后就不许要再考虑这个元素了


#
#     def heapify(self, nums, n, i):
#         '''
#         堆化操作，将数组转化为小根堆
#         :param nums: 完全二叉树对应的数组
#         :param n: 元素个数
#         :param i: 进行堆化的数组下标
#         '''
#         #取当前节点，将其与左右孩子中较大的元素进行调换
#         if i >= n:
#             return
#         c1, c2 = 2 * i + 1, 2 * i + 2
#         max = i  # 暂存最大数对应index
#         if c1 < n and nums[c1] > nums[max]:
#             max = c1
#         if c2 < n and nums[c2] > nums[max]:
#             max = c2
#         print(nums)
#         if max != i:
#             nums[i], nums[max] = nums[max], nums[i]
#             self.heapify(nums, n, max)
#
#     def build_heap(self, nums, n):
#         last_node = n - 1  # 堆化过程只需要考虑最后一个节点的父节点及其之前的节点
#         parent = (last_node - 1) // 2
#         for i in range(parent, -1, -1):
#             self.heapify(nums, n, i)
#
#     def heap_sort(self, nums, n):
#         self.build_heap(nums, len(nums))
#         print('build finished')
#         for i in range(n-1, -1, -1):
#             nums[i], nums[0] = nums[0], nums[i]  # 交换堆顶与最后一个元素，将交换后得到的最大数砍断
#             self.heapify(nums, i, 0)  # 后续操作一样，只不过后续的最大索引值变小了
#
#
nums = [4, 10, 3, 5, 1, 2]
s = HeapSort()
s.heap_sort(nums)
print(nums)










