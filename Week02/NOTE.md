学习笔记

[TOC]

#### 有效的异位词
1.直接对两个字符串进行排序，判断排序后的结果是否一致  
```
return sorted(s) == sorted(t)
```
2.根据两个字符串构建hash表，判断两个hash表是否一致  
```python
dic1, dic2 = {}, {}
for item in s:
    dic1[item] = dic1.get(item, 0) + 1
for item in t:
    dic2[item] = dic2.get(item, 0) + 1
return dic1 == dic2

```
3.只需要使用一个hash表，前一次遍历增加值，后一次遍历减少值  
最后判断hash表中的值是否为0
```python
if len(s) != len(t): return False
hashmap = {}
for substr in s:
    if not hashmap.get(substr):
        hashmap[substr] = 1
    else:
        hashmap[substr] += 1
for substr in t:
    if hashmap.get(substr):
        hashmap[substr] -= 1
    else:
        return False
for value in hashmap.values():
    if value != 0:
        return False
return True

```
4.使用python内置的count函数，统计字符出现的个数 原理与方法2一致

```python
if len(s) != len(t):
    return False
for i in set(s):
    if s.count(i) != t.count(i):
        return False
return True
```
优化
```python

if len(s)!=len(t):return False
tmp = set(s)
if tmp == set(t):#如果两个字符串的set相同进行深入判断
    for i in tmp:
        if s.count(i) != t.count(i): return False
    return True
return False
```

#### 异位词分组
对于给定包含多个字符串的列表，将其按照是否异位词分组输出  
1.由于异位词都是由相同字母集组成的，可以在遍历列表时，根据其字母排序是否一致，作为异位词分组的根据  
具体的 根据字母排序是否一致，构建hash表，以字母排序作为key(当然也可以使用字母的tuple序)，以原字符串作为键  
由于涉及到排序 所以时间复杂度为O(NKlogK),空间复杂度为O(NK)
```python
dic = {}
for item in strs:
    # key = tuple(sorted(item))#字母的键也可以用字母排序对应的tuple
    key = ''.join(sorted(item))#sorted返回的是list,不能作为dict的键
    if key in dic:
        dic[key].append(item)
    else:
        dic[key] = [item]
# return [x for x in dic.values()]#击败94%
return [dic[x] for x in dic]#击败97%
```
这种写法很直观，但是判断当前字符是否存在hash表中，有简简洁写法  
dict.get()获取不到时，返回[]   
获取到时 + [item]可以直接在原list中拼接  
```python
dic = {}
for item in strs:
    key = ''.join((sorted(item)))
    dic[key] = dic.get(key, []) + [item]
return [dic[x] for x in dic]
```
当然也可以使用defaultdict实现
```angular2html
dic = collections.defaultdict(list)
for item in strs:
    dic[tuple(sorted(item))].append(item)
return [dic[item] for item in dic]
```

2.根据字符串中字符出现的次数作为hash表的键  
对于每次遍历到的字符串，都需要维护一个长度为26的list，并要将其转化为tuple  
时间复杂度是O(NK),空间复杂度为O(NK)
```python
dic = {}
for item in strs:
    count = [0] * 26
    for char in item:
        count[ord(char) - ord('a')] += 1
    # res[tuple(count)].append(item)
    dic[tuple(count)] = dic.get(tuple(count),[]) + [item]
return [dic[x] for x in dic]
```
对应的defaultdict实现如下
```python
dic = collections.defaultdict(list)
for item in strs:
    count = [0] * 26
    for char in item:
        count[ord(char) - ord('a')] += 1
    dic[tuple(count)].append(item)
return [dic[x] for x in dic]
```

### 二叉树的深度优先遍历
递归实现都比较简单，也比较容易理解，不赘述

#### 二叉树的前序遍历 根左右

1.递归实现
```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if root:
        self.preorder(root, res)
    return res

def preorder(self, root, res):  # 前序遍历 根左右
    if root:
        res.append(root.val)
    if root.left:
        self.preorder(root.left, res)
    if root.right:
        self.preorder(root.right, res)
```
2.非递归实现
前序遍历的非递归实现应该是这三中遍历方式中最简单的  
首先将根节点置于stack中，在栈不为空的前提下，遍历整个二叉树  
每次先取出stack顶元素，如果栈顶元素不为None，就可以直接存入res中  
然后判断其左右子节点是否存在，并对他们进行入栈操作  
最后返回res

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    # 前序遍历的迭代实现
    if root is None: return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop()
        if cur is not None:
            res.append(cur.val)
            # 考虑到入栈的顺序，所以先右后左
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
    return res
```

#### 二叉树的中序遍历 左根右
1.递归实现
```python
def inorderTraversal(self, root):
    """
    #中序遍历 左根右
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if root:
        self.inorder(root, res)
    return res
def inorder(self, root, res):
    if root.left:
        self.inorder(root.left, res)
    if root:
        res.append(root.val)
    if root.right:
        self.inorder(root.right, res)
```

2.非递归实现
中序遍历的非递归实现就复杂一些了，因为每次并不是先将根节点的值输出，而是优先的找到树的最左子树  
所以要确保能一直往最左节点找 同时入栈 如果已经找到最左节点，  
那么首先应当将这个元素出栈存入res中 其次应判断当前栈顶元素是是否有右孩子 将cur指向栈顶元素的右孩子  
```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None: return []
    res, stack = [], []
    cur = root
    while cur is not None or stack:
        while cur is not None:  # 确保了能一直往左走
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()  # 相当于等到这次的根节点
        res.append(cur.val)
        cur = cur.right
    return res
```

#### 二叉树的后序遍历 左右根
1.递归实现
```python
def postorderTraversal(self,root):
    res = []
    if root is not None:
        self.postorder(root, res)
    return res
def postorder(self,root,res):
    if root.left is not None:
        self.postorder(root.left)
    if root is not None:
        res.append(root.val)
    if root.right is not None:
        self.postorder(root.right)
```
2.非递归实现
后续遍历的非递归方式应该是最难的，因为在入栈过程中还需要额外的指针标识是否已经访问过左子树的右孩子节点  
这里取巧使用两个栈，根节点不用在一个单独的栈中出入并用指针记录访问元素  

```python
def postorderTraversal(self, root):
    #用两个栈实现后序遍历的非递归实现
    if root is None:
        return False
    stack1,stack2 = [root], []
    while stack1:  # 找出后序遍历的逆序，存放在 stack2中
        node = stack1.pop()#每次取出的都是右子树节点值，进而在stack2中就相当于存储的是
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node.val)
    return stack2[::-1]
```

#### 二叉树的层序遍历
写着写着，才发现二叉树的层序遍历和我上面后序遍历是真的像
```python
class Solution(object):
    def levelTraversal(self,root):
        if root is None:
            return False
        stack1, stack2 = [root], []
        while stack1:  # 找出后序遍历的逆序，存放在 stack2中
            node = stack1.pop(0)#抛出第一个元素
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2#这里是层序遍历就不用反转了
```


#### N叉树的层序遍历
刚开始是这么写的，看起来算法逻辑没什么问题，但是这里我相当于是将cur当做一个list在做  
而实际上cur只是一个Node，哪怕它是root.children它也是个Node，所以没法将其进行迭代  
```python
def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        quene,res = [root],[]
        while quene:
            cur = quene.pop()
            if cur is not None:
                print(type(cur))#cur is Node
                #tmp = []
                #for item in cur:
                #   tmp.append(item.val)
                #res.append(tmp)
                res.append([item.val for item in cur])
                for child in cur.children:
                    quene.append(child)
        return res
```
改进之后，这里 实际上quene每次存储的都是每一层的所有节点，  
每次都将quene所有元素记录到tmp中，将所有节点合并为list之后存入res  
同时，在加入的过程中，用tmp_quene记录下一层的节点值，  
在遍历完上层节点后，将下层节点赋给quene
```python
def levelOrder(self,root):
    #击败55%
    if root is None: return []
    quene,res = [root],[]
    while quene:
    #将当前层的所有元素出队列，记录其值存入res中，由于输出格式的限制，要用tmp先存放
    #并且将其孩子全部记录在下一个quene中，这样保证了上层节点全部被加入到res中，而不会发生交替现象
        tmp, tmp_quene = [], []#这个tmp_quene是为了暂存下一层的所有节点
        for node in quene:
            tmp.append(node.val)
            for child in node.children:
                tmp_quene.append(child)
        res.append(tmp)
        quene = tmp_quene
    return res
```

#### N叉树的前序遍历
```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
      #dfs
    #   if not root: return []
    #   res = []
    #   self.dfs(root,res)
    #   return res 
    # def dfs(self,root,res):
    #     res.append(root.val)
    #     for node in root.children:
    #         self.dfs(node,res)
        #bfs 根左右
        if not root: return[]
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for node in cur.children[::-1]:
                stack.append(node)
        return res 

```

#### N叉树的后序遍历
```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # #dfs
        # if not root: return []
        # stack, res = [root],[]
        # while stack:
        #     cur = stack.pop()
        #     for node in cur.children:
        #         stack.append(node)
        #     res.append(cur.val)
        # return res[::-1]
        #dfs
        if not root: return []
        res = []
        self.dfs(root,res)
        return res
    def dfs(self, root, res):
        for node in root.children:
            self.dfs(node,res)
        res.append(root.val)
```

#### N叉树的最大深度
```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #DFS
        # if not root: return 0
        # if not root.children: return 1
        # tmp = [self.maxDepth(node) for node in root.children]
        # return max(tmp) + 1
        #bfs
        if not root: return 0
        # if not root.children: return 1    
        stack, depth = [root], 0
        while stack:
            depth += 1
            for i in range(len(stack)):
                cur = stack.pop(0)
                for node in cur.children:
                    stack.append(node)
        return depth 
```

#### 二叉树的最大深度
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #bfs
        if not root: return 0
        stack, depth = [root], 0
        while stack:
            for i in range(len(stack)):
                cur = stack.pop(0)#注意到这里和后序遍历 层序遍历一致 都是pop(0)
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
            depth += 1
        return depth
       #dfs
    #    if not root: return 0
    #    return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
       
```

#### 二叉树的最小深度
```python

```


#### 数组中最小的k个数
1.暴力解法 对数组进行排序，返回前k个
```python
arr.sort()
return arr[:k]
```
2.小根堆 借助python内置的heapq实现
```angular2html
if k == 0:
    return []
heap = [-x for x in arr[:k]]  # 只用维护一个大小为k的小根堆
heapq.heapify(heap)  # 这k个元素一定满足三角顶最小的原则
for i in range(k, len(arr)):
    if -heap[0] > arr[i]:
        heapq.heappop(heap)  # 如果堆中的元素大于入堆元素，则将原堆顶元素出堆
        heapq.heappush(heap, -arr[i])  # 将这个元素放入小根堆中，heappop中调用了siftup调整了堆
res = [-x for x in heap]
return res
```
3.快排思想
```python
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
```

#### 堆排序
堆排序的过程主要包括 建堆以及对每一个小三角形进行堆化处理，使之满足小根堆或者大根堆的情形  
建堆是指，对于给定的元素，从下往上考虑（从最后一个非叶节点开始）使之满足nums_i>(nums_2xi+1,nums_2i+2)  
然后对于每一个元素 逆序遍历时 与堆的根节点进行调换 对树进行从上往下的堆化比较过程  
对于有节点值交换的情形 进一步考量它的下一层是否符合小根堆或大根堆的条件  
建堆之后 堆顶的元素应该是最大的(大根堆)，此时将它与末尾元素调换就会使得最大元素到最后位置，对现今的堆顶元素进行堆化  
这个过程就完成了对一个元素的排序，目前堆中的最大元素已经到了末尾，下一次进行调整时就无须再处理此元素  
```python

#时间复杂度为NlogN，logN为建立大根堆/小根堆的时间复杂度，
#heapify的时间复杂度是O(logN)的因为，最坏情况下，每一层都需要判断
#N为对已经构成的堆排序反向遍历的时间复杂度

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
    print(nums)

    for i in range(size-1,0,-1):#排序需要对整个堆进行调整
        nums[i], nums[0] = nums[0], nums[i]#交换末尾元素与堆顶元素
        self.heapify(nums,i,0)#交换之后，要确定这个堆是否合乎条件，进行堆化，
        #要注意到，每次堆化时，就已经把一个元素排好了，放在最末尾了，以后就不许要再考虑这个元素了
```


#### 判断是否是丑数
如果一个数是丑数那肯定满足这种定义num = 2^i*3^j*5^k
```python
if num == 0: return False
while num % 5 == 0: num /= 5
while num % 3 == 0: num /= 3
while num % 2 == 0: num /= 2
return num == 1#击败98%，省去了迭代的过程
```
当然也可以简化为如下，但是就要多一部分迭代过程
```angular2html
for item in [2,3,5]:
    while num%item==0:#依次除尽2，3，5
        num = num/item
# return True if num==1 else False #击败50%
# return num==1#击败87%
```

#### 求第n个丑数
动态规划的题，解法分 动态转移方程和动态转移矩阵
后面整理一套解法
```python
# 1、2、3、5、4、6、8、9、10
if n==0:
    return 0
res = [1]*n
p2,p3,p5 = 0,0,0#指向三个队列的指针
for i in range(1,n):
    res[i] = min(res[p2]*2,res[p3]*3,res[p5]*5)
    if res[i] == res[p2]*2: p2 = p2+1
    if res[i] == res[p3]*3: p3 = p3+1
    if res[i] == res[p5]*5: p5 = p5+1
return res[-1]
```

#### 验证字符串是否是回文串
1.翻转字符串 看是否相同 击败81%
```python
tmp = "".join(char.lower() for char in s if ch.isalnum())
return tmp == tmp[::-1]
```
2.双指针 击败61%
```angular2html
tmp = "".join(char.lower() for char in s if ch.isalnum())
n = len(tmp)
left, right = 0, n - 1
while left < right:
    if tmp[left] != tmp[right]:
        return False
    left, right = left + 1, right - 1
return True
```

#### 正则表达式匹配
1.递归解法  
是超出时间限制的，时间复杂度是O(3^N)
```python
def isMatch(self, s: str, pattern: str) -> bool:
    # 特殊情况处理
    if len(s) == 0 and len(pattern) == 0: return True
    if len(s) > 0 and len(pattern) == 0: return False
    # 如果pattern形如 a*####，检查这个*能匹配几次
    if len(pattern) > 1 and pattern[1] == '*':#击败80%
        # s和pattern首字母相同
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
            # s能和pattern匹配的情形
            # 1.*匹配0次，则需要递归的对s和pattern[2:]进行匹配
            # 2.*匹配1次，需要递归的对s[1:]和pattern[2:]进行匹配
            # 3.*匹配n次，需要递归的对s[1:]和pattern进行匹配
            return self.isMatch(s, pattern[2:]) or self.isMatch(s, pattern[2:]) or self.isMatch(s[1:], pattern)
        else:  # 如果首字母不相同，就相当于*匹配0次，继续匹配s和pettern[2:]
            return self.isMatch(s, pattern[2:])
    # pattern以.开头
    if len(s) > 0 and (pattern[0] == '.' or s[0] == pattern[0]):
        return self.isMatch(s[1:], pattern[1:])
    return False
```
python中有装饰器优化迭代过程@lru_cache  
所以在函数前使用装饰器即可通过
```python
@lru_cache
def isMatch(self, s: str, pattern: str) -> bool:
    pass
```
上面的代码比较复杂，可以优化代码
```angular2html
if not pattern: return not s#这句话真的优秀
match_first = bool(s) and (pattern[0] == s[0] or pattern[0] == '.')
if len(pattern) > 1 and pattern[1] == '*':
    return (self.isMatch(s, pattern[2:]) or match_first and self.isMatch(s[1:], pattern))
else:
    return match_first and self.isMatch(s[1:], pattern[1:])
```
2.动态规划
```python
pass
```


#### 只出现一次的数字 时间复杂度为O(N)，空间复杂度为O(N)
除一个数外，所有元素都出现了两次，求这个只出现一次的元素
1.两次hash表 遍历list，用hash表统计每个值出现的次数，根据出现次数返回key
```python
# 1.hash表记录出现次数，以num为key，以出现次数为value 击败42%
dic = {}
for num in nums:
    dic[num] = dic.get(num,0)+1
for key, value in dic.items():
    if value == 1:
        return key
```
2.题目要求用常数级的空间复杂度实现，则不能用hash表实现
```python
#位运算，击败97%
# 由于每个元素都出现了两次，根据异或运算可以消去这两个元素
#最后保留的就是带求值key和初始值1的异或
res = 0
for num in nums:
    res ^= num
return res
```

#### 只出现一次的数字II
1. 数学计算
```python
tmp = set(nums)
return (3*sum(tmp) - sum(nums))//2
```
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。  
1.python解法 使用count函数 但是count函数本身的时间复杂度就是O(N)的，导致算法时间复杂度是O(N^2)
```python
for num in nums:
    if nums.count(num)==1:
        return num
```
对应的优化是采用collections中的Counter模块
```python
from collections import Counter
dic = Counter(nums)
for key in dic.keys():
    if dic[key] == 1:
        return key
```
2.hash表法 通用解
```python
dic = {}
for num in nums:
    dic[num] = dic.get(num,0)+1
for key, value in dic.items():
    if value == 1:
        return key
```
3. 借助逻辑电路，构造这样的逻辑门状态  
1x1x1->1 1->0，这个数可以出现0次、1次、2次，需要两位来表示其状态  
构造真值表 写出逻辑表达式 并化简  
参考连接[电路逻辑通俗解](https://leetcode-cn.com/problems/single-number-ii/solution/luo-ji-dian-lu-jiao-du-xiang-xi-fen-xi-gai-ti-si-l/)
```python
x,y = 0,0
for z in nums:
    tmp = ~x&(y^z)
    x = (x&~y&~z)|(~x&y&z)
    y = tmp
return y
```
根据两个表达式同构的性质，可以优化更新x的逻辑表达式
```python
x, y = 0, 0
for num in nums:#num means input
    y = ~x & (y^num)
    x = ~y & (x^num)
return y
```

#### 只出现一次的数字III
1.使用Counter
```python
from collections import Counter #{'num':count}
dic = Counter(nums)
return [key for key in dic if dic[key]==1 ]
```
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。  
2.hash表法
```python
dic,res = {}, []
for num in nums:
    dic[num] = dic.get(num,0) + 1
for key,value in dic.items():
    if value == 1:
        res.append(key)
return res
```
3.接上一题的思路，如果对这些元素进行异或，得到的结果就是待求元素的异或值，如何从结果中分离这两个元素呢？  
异或得到的结果不能直接分离出待求元素，但是我们可以根据这个异或值的第一个1将原数组分类，  
由于其余元素都是出现两次的，所以对这两个数组分别求异或即可得到结果。
```python
tmp = 0
for num in nums:
    tmp ^= num
#找到第一位不相同的数字
count = 0
while tmp&1 !=1:
    tmp>>=1#右移1位
    count += 1
tmp1,tmp2 = [],[]
for num in nums:
    if num>>count & 1 == 0:#将该数向右移动count位
        tmp1.append(num)
    else:
        tmp2.append(num)
res = []
t1,t2 = 0,0
for num in tmp1:
    t1 ^= num
res.append(t1)
for num in tmp2:
    t2^= num
res.append(t2)
return res

```
上面的方式可以优化，其一，找第一位不同，第二，不需要用数组存放元素，直接根据此位是否为1，直接进行计算
```python
tmp= 0
for num in nums:
    tmp ^= num
# rightmost 1-bit diff between x and y
diff = tmp & (-tmp)#这个找到第一位不相同的方式厉害
x = 0
for num in nums:
    if num & diff:#结果大于0执行，此位为1为一组，直接计算
        x ^= num
return [x, tmp^x]#tmp是两个数的异或值，一个值已经找到了
```

#### 二叉树的最大路径和
比较自然的想法是递归，计算上层节点的最大路径时，只需要考虑左右子树最大值  
路径： 左->中->再上  
      左->中  
      左->中->右    
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
class Solution:
    def __init__(self):
        self.maxpath_sum = float("-inf")#节点值可能为负值

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxGain(root)
        return self.maxpath_sum

    def maxGain(self,node):
        if not node: return 0
        left_gain = max(self.maxGain(node.left),0)#将空值、负值过滤掉了
        right_gain = max(self.maxGain(node.right),0)
        path_sum = node.val + left_gain + right_gain #左根右
        self.maxpath_sum = max(path_sum, self.maxpath_sum)#更新self.maxpath_sum，过滤负值
        return node.val + max(left_gain, right_gain)#对于更上层的元素，它的最大路径值，只可能向左或向右到达此节点，所以取最大值
```
