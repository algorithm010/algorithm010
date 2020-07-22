学习笔记

#### 两数之和
1.暴力解法 两次遍历枚举出所有可能的数的配对 时间复杂度是O(N^2)
    两重循环的标准写法：

```python
for i in range(len(nums)-1):#给第二个指针预留一个位置
for j in range(i + 1, len(nums)):#这里从第一个指针的下一个位置开始
    if nums[i] + nums[j] == target:
        return [i, j]
```

2.两次hash表 第一次遍历数组，将所有元素的对应解`target-nums[i]`作为`key`存入hash表中
    下一次遍历此数组时，查询hash表中的内容

```python
dict = {}
for ind, num in enumerate(nums):  # 创建hash表
    dict[num] = ind
for ind, num in enumerate(nums):  # 遍历hash表
    j = dict.get(target - num)
    if j and ind != j:  # 排除[2,3] 4这种情况
        return [ind, j]
```
3.一次hash表 上面的两次hash表中，会存表示同样一组解的情形，比如`{'2':4}`和`{'4':2}`，所以可以在一次遍历时，先判断是否在hash表中，不在则加入；在即返回对应结果

```python
dict = {}
for ind, num in enumerate(nums):
    if dict.get(target - num) is not None:
        return [dict.get(target - num), ind]
    dict[num] = ind
```

--

#### 三数之和
1.同样可以采用暴力解法，三重循环枚举出所有可能的三元组，时间复杂度是O(N^3)
    三重循环的标准写法：

```python
nums.sort()
res = set()
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for m in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[m] == 0:
                res.add((nums[i],nums[j],nums[m]))
return list([list(item) for item in res])
```

2. 排序+set去重+两次循环+二重循环+hash表
    第一次遍历时，构建hash表 `{'nums[i]':ind}`  
    第二次循环，枚举可能的二元组，同时查询hash表检测是否存在  

```python
hashmap = {}
nums.sort()
res = set()
for ind, num in enumerate(nums):
    hashmap[num] = ind
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        target = 0 - nums[i] - nums[j]
        if hashmap.get(target) is not None and hashmap[target] > j:
            # Only need to check if the target value on the right side of (j)
            res.add((nums[i], nums[j], target))
return list(res)
```

3. 排序+set去重+双指针+过滤解+排序数组首元素过滤正数优化

```python
nums.sort()
res = []
for i in range(len(nums)-2):
    if nums[i]>0:#plus this line ,you can beat 93%
        break
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left, right = i + 1, len(nums) - 1
    while (left < right):
        tmp = nums[i] + nums[left] + nums[right]
        if tmp < 0:
            left = left + 1
        elif tmp > 0:
            right = right - 1
        else:
            res.append((nums[i], nums[left], nums[right]))
            while (left < right) and nums[left] == nums[left + 1]:
                left = left + 1
            while (left < right) and nums[right] == nums[right - 1]:
                right = right - 1
            left = left + 1 #put the two lines, you can
            right = right - 1
return res
```

--

#### 移动0
1.暴力解法 遇到则将0移动到数组末尾
    每次遇到0，先加入到末尾，再删除这个0以调整数组，时间复杂度O(N^2)  

```python
for num in nums:
if num == 0:
    nums.append(0)
    nums.remove(0)
```

2.统计0的个数 同时删除这个0 如果不为0 则将它放到前面那个0的位置
    最后返回数组时，将count个0放到数组的末尾len-count开始的count个位置

```python
count = 0
for i in range(len(nums)):
    if nums[i]==0:
        count = count + 1
    else:#[0,1,0,3,12]
        nums[i-count] = nums[i]
for i in range(len(nums)-count,len(nums)):
    nums[i] = 0
```

3.用指针记录当前0的个数 遇上不为0的数，则将它与前面记录的0的位置的元素进行交换

```python
index_0 = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[index_0], nums[i] = nums[i], nums[index_0]
        index_0 = index_0 + 1
return nums
```

--

#### 爬楼梯
1.蠢递归

```python
if n == 1: return 1
if n == 2: return 2
return self.climbStairs(n - 1) + self.climbStairs(n - 2)    
```    

2.递归+数组备忘录

```python
if n == 1: return 1
tmp = [0 for _ in range(n)]  # 开辟额外数组空间
tmp[0], tmp[1] = 1, 2
for i in range(2, n):
    tmp[i] = tmp[i - 1] + tmp[i - 2]
return tmp[-1]
```

3.递归+变量缓存

```python
if n == 1: return 1
a, b = 1, 2
for i in range(2, n):
    a, b = b, a + b
return b
```

--

#### 容器的最大面积
1.暴力枚举所有可能的面积 时间复杂度O(N^2)

```python
max_area = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            area = (j - i) * min(height[j], height[i])
            if max_area < area: max_area = area
    return max_area
```

2.双指针

```python
left,right,area = 0,len(height)-1,0
while left<right:
    if height[left] < height[right]:
        area = max(area,height[left]*(right-left))
        left += 1# 往右找看是否有较高的板子
    else:
        area = max(area,height[right]*(right-left))
        right -= 1
return area
```

--

#### 检测链表是否有环
1.快慢指针 跑操场

```python
if not head or not head.next:
    return False
fast, slow = head.next, head
while fast != slow:  # 相遇的时候退出此while返回True
    if fast == None or fast.next == None:
        return False
    fast = fast.next.next
    slow = slow.next
return True
```

2.hash表存储遍历过的节点

```python
hashtable = {}
if not head or not head.next:
    return False
while head:  # 如果遍历完链表，则返回False
    if hashtable.get(head):
        return True
    else:  # 如果该节点没有出现过，则将其存入hashtable中
        hashtable[head] = True
        head = head.next
return False
```

--

#### 检测链表是否有环+指出环的入口
1. 双指针+重开指针

```python
def detectCycle(self, head: ListNode) -> ListNode:
    fast = slow = finder = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            while slow != finder:
                slow, finder = slow.next, finder.next
            return slow
    return None
```

2. hash表

```python
hashtable = {}
while head:
    # if not in the hashtable
    if not hashtable.get(head):
        hashtable[head] = head
        # must move back the head pointer, so it can continue while loop
        head = head.next
    else:
        # if the node in hashtable, it must be the loop header
        return head
# if walk here head==None, so we just return None
return None
```

--

#### 加一
判断进位，如果末位是9->末位修改为0 继续判断
如果不为0，则该位置+1后return即可
如果出现999这种情形，那循环只会讲digits处理为000，需要在前面添1

```python
for i in range(len(digits)-1,-1,-1):
    if digits[i] != 9:
        digits[i] += 1
        return digits
    digits[i] = 0 #[9,9,9,9]的情况处理完再返回
return [1]+digits    
```


--

#### 旋转数组
1. 切片后重新赋值

```python
#tmp = nums[len(nums) - k:] + nums[:len(nums) - k]
#for i in range(len(tmp)):#这种赋值就比较傻
#    nums[i] = tmp[i]

k = k % len(nums)#要考虑k大于数组长度的情形
nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
```

2.暴力解法 类似于bubble排序，k轮交换(从后往前)，每一轮中交换len(nums)次

```python
for i in range(k%len(nums)):  # 旋转k次
    for j in range(len(nums) - 1, 0, -1):#反序调转
        nums[j - 1], nums[j] = nums[j], nums[j - 1]
```

3.reverse三次，先reverse整个List，再reverse List[:k] 第三次reverse List[k:]


4. 最大公约数解法，还未掌握

--

#### 合并两个有序数组
1.暴力解法 将两个数组合并后重新排序

```python
nums1[:] = sorted((nums1[:m] + nums2))
```
2.两个指针分别指向数组的最小元素，将较小的元素放入nums1中

```python
tmp = nums1[:m]
nums1[:] = []#注意这里要重新赋值，而不能只是传递引用
i, j = 0, 0
while i < m and j < n:
    if tmp[i] < nums2[j]:
        nums1.append(tmp[i])
        i = i + 1
    else:
        nums1.append(nums2[j])
        j = j + 1
if i < m:#tmp数组中还有剩余元素
    nums1[i+j:] = tmp[i:]
if j < n:
    nums1[i+j:] = nums2[j:]
```
3.两个指针指向数组的最大元素，将较大的元素插入到nums1末尾，无需额外的开辟数组空间

```python
i, j = m-1, n-1
ind = m+n-1
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[ind] = nums1[i]
        ind, i = ind-1, i-1
    else:
        nums1[ind] = nums2[j]
        ind, j = ind-1, j-1
#如果nums1中还有元素不需要处理
#而如果是nums2中还有元素，那么说明nums1中前面的元素需要被替换
nums1[:j+1] = nums2[:j+1]
return nums1
```

--

#### 合并两个有序链表

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:#如果l1为空，直接返回l2
            return l2
        if not l2:#如果l2为空，直接返回l1
            return l1
        rhead = ListNode(None)#用来返回最后的结果的节点
        pre = rhead #用来添加比较过的节点
        while l1 and l2:#循环直到某链表没有值结束,刚开始这里写的是l1.next and l2.next 返回的结果是[1,1,2,4]
            if l1.val <= l2.val:
                tmp,l1 = l1,l1.next#
                pre.next = tmp
                pre = tmp
            else:
                tmp,l2 = l2,l2.next
                pre.next = tmp
                pre = tmp
        if not l1:
            pre.next = l2
        if not l2:
            pre.next = l1
        return rhead.next
```

#### 删除排序数组中的重复数
1.双指针 用指针记录不同元素的个数 思路比较天马行空 但是有迹可循 就是 用一个指针记录当前不同元素的个数，每次不相同时，就将这个指针更新，并且将num[i+1]赋值给指针指向的地址

```python
point = 0 # 指向前一个重复的数值
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        continue
    else:
        point = point + 1
        nums[point] = nums[i+1]
return point+1
```

#### 最长公共前缀
1. 先确定列表中最短字符串的长度size LCP应该小于等于它 然后外层循环遍历size长度，内层循环取每个字符的前size位，如果所有的都相匹配，则返回

```python
if not strs: return ''
min_size = min([len(x) for x in strs])  # 公共前缀最长只会这么长
for i in range(min_size, 0, -1):
    tmp = strs[0][:i]  # 当前待比较的公共前缀子串
    if all(s[:i] == tmp for s in strs):
        return tmp
return ''
```
改进版
```python
prefix = strs[0] if strs else ''
while True:
    if all(s.startswith(prefix) for s in strs):
        return prefix
    prefix = prefix[:-1]
```
