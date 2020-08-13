学习笔记
判断奇偶 
x&1 == 1 if odd else even
x = x & (x-1) 清除最右的1
x = x & (-x) 得到最右的1

#### 位为1的个数
给一个无符号整数，返回其二进制表示中1的个数  
1. 先转二进制，匹配二进制字符串中1的个数，最后返回
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        tmp = bin(n)[2:]
        count = 0
        for i in range(len(tmp)):
            if tmp[i] == '1':
                count += 1
        return count
```
2.判断最低位是否为1，然后右移一位，继续判断
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!=0:
            if n & 1 == 1:#判断最低位是否为1
                count += 1
            n = n >>1
        return count
```
3.直接找到最低位的1，看能找几次
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!=0:
            n = n & (n-1)#清除最低位的1
            count += 1
        return count
```

#### 二的幂
判断是否是2的幂次
1.辗转相除法，直到结果为1为止
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False#与面试官沟通边界
        if n==1: return True
        while n!=1:
            if n%2!=0: return False
            else: n = n//2
        return True
```
2.如果是2的幂次，那么其二进制位应该有且仅有一个1.
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        while n!=0:
            return (n&(n-1))==0 #打掉最后一个1看是否为0 以此检查是否只有一个1
```

#### 颠倒二进制位
想法是将二进制位里面的第i为调换到31-i位上，然后用加法累计所有位的调换  
从右向左遍历，然后将数左移以调换  

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res,power= 0,31
        while n:
            res += (n&1)<<power#只管最后一位是0还是1
            n = n>>1#以取得新的最后一位
            power -= 1
        return res
```

#### 布隆过滤器
布隆过滤器常用作 防止缓存击穿情况的出现 预先判断数据是否存在数据库中，可以缓解对数据库的压力  
布隆过滤器的思想是，利用一个二进制数组，对于任何一个value，我们都给他它分配一个定长的k位二进制数，可以不连续  
每次有元素进来，就使用特定的hash函数生成k个01，代表它的二进制描述，  
在查找的时候，如果待查元素不在布隆过滤器中，说明一定不存在，反之说明可能存在  
```python
from bitarray import bitarray
import mmh3
class BooleanFilter:
    def __init__(self,size,hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray
        self.bit_array.setall(0)
    def get(self,x):
        for seed in range(self.hash_num):
            result = mmh3.hash(x,seed)%self.size#用k位二进制表示是否存在
            self.bit_array[result] = 1
    def lookup(self,x):
        for seed in range(self.hash_num):#检查x的每一位的0，1，只要不是1，就不在
            result = mmh3.hash(x,seed)%self.size
            if self.bit_array[result] != 1:
                return 'not in'
        return 'probably in'
```  

####  LRUcache 
最近最久未使用算法，例如手机后台切换的时候看到的算法  
实现起来是利用hash表+双向链表  
注意到这个双向链表维护了两个节点并不存值，是head和tail  
每次有新的元素进来，如果capicity还有容量，就加入到双向链表**首部**   
如果没有容量了，就从双向链表末尾删除一个元素  
如果新进来的元素在双向链表中[这就是为什么要使用hash表的原因，查在不在hash表中O(1)]  
就先拿出来，修改值，再插入到双向链表**首部**  
>实现的时候就是要实现两个函数insert和delete

```python
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        node = self.dic[key]
        self.delete(node)#访问过后要将它放到链表头部
        self.insert(node)
        return node.val

    def insert(self,node):
        node.next, node.prev = self.head.next, self.head
        temp = self.head.next
        self.head.next = node
        temp.prev = node

    def delete(self,node):
        node.prev.next, node.next.prev = node.next, node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.dic:#如果相同key值出现过，更新dic和链表
            node = self.dic[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            return
        if len(self.dic) == self.capacity:
            node=self.tail.prev#删除第一个元素
            self.delete(node)
            del self.dic[node.key]
        node = ListNode(key,value)#将此元素加入到第一个元素
        self.dic[key] = node
        self.insert(node)
```

#### 归并排序
归并排序的思想就是分治到单个元素，然后回头 治理 回头的时候就有左右两个子数组已经有序了  
主要就是实现的时候需要用额外的空间
```python
class Solution:
    def merge_sort(self, nums):
        if len(nums)<2:
            return nums
        mid = len(nums)//2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        return self.merge(self.merge_sort(nums1), self.merge_sort(nums2))

    def merge(self, nums1, nums2):
        res = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))
        while nums1:
            res.append(nums1.pop(0))
        while nums2:
            res.append(nums2.pop(0))
        return res
```
#### 快速排序
快速排序的思想是界定一个pivot，找到左边比pivot大的找到右边比pivot小的，交换  
使得每一轮排序后，左右数组符合左数组<pivot<右数组  
```python
class Solution:
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        ind = left + ((right-left) >> 1)
        pivot = self.partition(nums, left, right, nums[ind])
        self.quick_sort(nums, left, pivot-1) #左
        self.quick_sort(nums, pivot, right) #右

    def partition(self, nums, left, right, pivot):
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        return left
```

#### 堆排序
首先从右往左遍历，使得每个小三角的顶最大，这是建堆   
前边建堆nums[0]最大，我们把最大的元素与末尾交换，然后调整堆[只用调整除末尾元素外的]   
```python
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
```


#### 数组的相对排序
就是把arr1的元素按这样的规律排序：如果arr1[i]在arr2中，就将其在arr2中的相对位置排序  
如果不在，则按大小排序  
思路就是，将arr1元素记录在hashmap中，遍历arr2，修改arr1，这样必然可以满足在arr2中的元素，按其在arr2中的顺序排序  
对于不在的，拿出来排序再赋值到arr1中  
```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        for i, num in enumerate(arr1):
            hashmap[num] = hashmap.get(num,0) + 1
        ind = 0
        for i in range(len(arr2)):
            cur = arr2[i]
            while hashmap.get(cur) > 0:
                arr1[ind] = cur
                hashmap[cur] -= 1
                ind += 1
        # 将不在arr2中的元素升序排列，但由于不是有序字典
        tmp = []
        for key, val in hashmap.items():
            while val > 0:
                tmp.append(key)
                hashmap[key] -= 1
                val -= 1
        tmp.sort()
        arr1[ind:] = tmp
        # return arr1[:ind] + tmp
        return arr1
```

#### 区间合并
给定一个区间集合，合并所有重叠的区间  
这一题如果没做过，真不简单  
秒解是 **先按照左区间排好序** 这样有两个好处  
1所有可以合并的区间必然相连 2合并时只用看前边的区间右值与当前区间的左值的大小
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #按区间左端点值进行排序，那么能合并的区间必然相连
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:#res[-1]区间右值小于起始值
                res.append(interval)    
            else:#否则更新右值
                res[-1][1] = max(res[-1][1],interval[1])
        return res
```

#### 493 翻转对

#### 315 计算右侧小于当前元素的个数

#### 剑指offer51 数组中的逆序数对
```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        temp = [0 for _ in range(size)]
        return self.reverse_pairs(nums, 0, size - 1, temp)

    def reverse_pairs(self, nums, left, right, temp):#在数组 nums 的区间 [l,r] 统计逆序对
        if left == right:
            return 0
        mid = left + ((right-left) >> 1)
        lpairs = self.reverse_pairs(nums, left, mid, temp)
        rpairs = self.reverse_pairs(nums, mid + 1, right, temp)
        cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
        return lpairs + rpairs + cross_pairs

    def merge_and_count(self, nums, left, mid, right, temp):
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i,j,count = left, mid+1,0
        for k in range(left, right + 1):
            if i == mid + 1:#左侧处理完之后
                nums[k] = temp[j]
                j += 1
            elif j == right + 1:#右侧处理完之后
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:#前边的小，不用计数，将前边的值归并到temp中
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]#后边的小，将后边的值归并到tmp中，累计计数值
                j += 1
                count += (mid - i + 1)#
        return count

```

