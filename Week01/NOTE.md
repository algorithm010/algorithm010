学习笔记

#### 两数之和
1.暴力解法 两次遍历枚举出所有可能的数的配对 时间复杂度是O(N^2)
    两重循环的标准写法：
    
```
for i in range(len(nums)-1):#给第二个指针预留一个位置
for j in range(i + 1, len(nums)):#这里从第一个指针的下一个位置开始
    if nums[i] + nums[j] == target:
        return [i, j]
```
    
2.两次hash表 第一次遍历数组，将所有元素的对应解`target-nums[i]`作为`key`存入hash表中
    下一次遍历此数组时，查询hash表中的内容
    
```
dict = {}
for ind, num in enumerate(nums):  # 创建hash表
    dict[num] = ind
for ind, num in enumerate(nums):  # 遍历hash表
    j = dict.get(target - num)
    if j and ind != j:  # 排除[2,3] 4这种情况
        return [ind, j]
```
3.一次hash表 上面的两次hash表中，会存表示同样一组解的情形，比如`{'2':4}`和`{'4':2}`，所以可以在一次遍历时，先判断是否在hash表中，不在则加入；在即返回对应结果

```
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
    
```
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
      
```
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

```
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
    
```
for num in nums:
if num == 0:
    nums.append(0)
    nums.remove(0)
```

2.统计0的个数 同时删除这个0 如果不为0 则将它放到前面那个0的位置 
    最后返回数组时，将count个0放到数组的末尾len-count开始的count个位置
    
```
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

```
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

```
if n == 1: return 1
if n == 2: return 2
return self.climbStairs(n - 1) + self.climbStairs(n - 2)    
```    

2.递归+数组备忘录

```
if n == 1: return 1
tmp = [0 for _ in range(n)]  # 开辟额外数组空间
tmp[0], tmp[1] = 1, 2
for i in range(2, n):
    tmp[i] = tmp[i - 1] + tmp[i - 2]
return tmp[-1]
```

3.递归+变量缓存

```
if n == 1: return 1
a, b = 1, 2
for i in range(2, n):
    a, b = b, a + b
return b
```

--

#### 容器的最大面积
1.暴力枚举所有可能的面积 时间复杂度O(N^2)

```
max_area = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            area = (j - i) * min(height[j], height[i])
            if max_area < area: max_area = area
    return max_area
```

2.双指针 

```
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

```
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

```
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

```
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

```
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




