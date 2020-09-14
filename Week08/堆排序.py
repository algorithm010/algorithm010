# # -*- coding:utf-8 -*-
# # Author : Ray
# # Data : 2020/7/28 9:04 PM
#
# 不稳定
class Solution:
    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums)-1,-1,-1):#调整堆的时候将最大的元素nums[0]放到最后面，
            nums[i],nums[0] = nums[0],nums[i]
            self.heapify(nums,i,0)

    def build_heap(self, nums):#使得每个小三角形都是顶最大
        for i in range(len(nums)-1//2,-1,-1):
            self.heapify(nums,len(nums), i)

    def heapify(self, nums, n, i):
        if i >= n: return
        c1, c2 = i*2+1, i*2+2
        ind = i
        if c1 < n and nums[c1] > nums[ind]:
            ind = c1
        if c2 < n and nums[c2] > nums[ind]:
            ind = c2
        if ind != i:
            nums[i], nums[ind] = nums[ind], nums[i]
            self.heapify(nums,n,ind) #调整堆之后要继续保持堆的特性


s = Solution()
nums = [2,3,1,4,2,5,6,8,6,5,7]
s.heap_sort(nums)
print(nums)
