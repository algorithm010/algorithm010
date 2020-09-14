# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/31 7:03 PM

class SolutionI:

    def merge_sort(self,nums):
        # 递归终止条件 左右子数组长度为1的时候返回该数组
        if len(nums) <2: return nums
        #归并排序 左右都已经排好序合并两个
        mid = len(nums)//2
        # nums1 = nums[:mid]
        # nums2 = nums[mid:]
        return self.merge(self.merge_sort(nums[:mid]),self.merge_sort(nums[mid:]))


    def merge(self,nums1,nums2):
        res = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))

        while nums1:
            res.append(nums1.pop(0))
        while nums2:
            res.append(nums2.pop(0))
        return res


class SolutionII:

    def quicksort(self,nums,left,right):
        #快速排序，partition返回下标
        # left,right = 0, len(nums)
        if left >= right: return
        # pivot = nums[mid]
        mid = left + ((right-left)>>1)
        pivot = self.partition(nums,left,right,nums[mid])
        self.quicksort(nums,left,pivot-1)#左
        self.quicksort(nums,pivot,right)#右
        return nums

    def partition(self,nums,left,right,pivot):
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left],nums[right] = nums[right],nums[left]
                left,right = left+1,right-1
        return left


class SolutionIII:
    def heapsort(self,nums):
        self.build_heap(nums)
        for i in range(len(nums)-1,-1,-1):#从后往前遍历，把最大的放到最后
            #这里要交换!
            nums[i],nums[0] = nums[0],nums[i]
            self.heapify(nums,i,0)

    def build_heap(self,nums):
        for i in range(len(nums)//2):#建堆错了没？？，应该是从后往前建堆，因为后面的堆调整后要继续向前
            self.heapify(nums,len(nums),i)

    def heapify(self,nums,n,i):
        #少了递归终止条件
        if i >= n: return
        c1,c2 = i*2+1,i*2+2
        max_ind = i
        #堆排序内部，是没有for循环的只有递归
        if c1 < n and nums[c1] > nums[max_ind]:
            max_ind = c1
        if c2 < n and nums[c2] > nums[max_ind]:
            max_ind = c2
        if i != max_ind:#这里的条件记清楚了！
            nums[max_ind], nums[i] = nums[i], nums[max_ind]
            self.heapify(nums, n, max_ind)#调整后继续维持堆


s = SolutionI()
nums = [2, 3, 1, 4, 2, 5, 6, 8, 6, 5, 7]
res = s.merge_sort(nums)
print(res)


# 1.想办法合并这几个数组，合并的规则是
# merge =[0,...,max_n]
# [a1...a2] [b1...b2]
def maxK(nums,n):
    #但是这种方法不能解决 15 23 15 24 的情形，所以要动态的创建set，依次判断是否在set中
    # 即使是 15 23 15 24
    # 求出所有课程中耗时最长的，构建一个数组存放，记录课程起止时间出现的次数，返回数组中的最大计数
    size = max(max(nums))
    tmp = [0]*(size+1)
    for num in nums:
        for cur in num:
            tmp[cur] += 1
    return max(tmp)


# 2.最终奖励值 等于自己选的 加上 从剩余的中选的最大值 |或者干脆就不选，如果不选，其他人的奖励值就只由取到的奖券面额决定
# f[n] = f[n-1]+nums[n] f[n]代表第n-1个同学能拿到的最大面值
# 动态规划方程出来了


size = 40
a = 30
b = 10

def tickets(size,a,b):#a,b分指50 和 100
    count = 0
    start = 1

    return count


def dfs(size, a, b, cur, count, start):
    if cur < 0: return
    if start == size: return count
    cur += 50
    while start < size:
        dfs(size,a - 1,b,cur,count)









