# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/14 6:41 PM

nums = [2,5,5,2,4,4]
size = len(nums)
delta = 1000
for i in range(size):
    times = nums[i] %delta
    nums[times] += delta
    nums[i] -= times
    print(nums)
MAX=0
res=0
for i in range(size):
    print("数字",i,"在数组中出现的次数：",nums[i]//delta)
    if MAX <= nums[i]//delta:
        MAX = nums[i]//delta
        res = i
print("出现次数最多的数字",res)