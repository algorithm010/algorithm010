学习笔记

#### 有效的异位词
1.直接对两个字符串进行排序，判断排序后的结果是否一致
```
return sorted(s) == sorted(t)
```
2.根据两个字符串构建hash表，判断两个hash表是否一致
```angular2html
dic1, dic2 = {}, {}
for item in s:
    dic1[item] = dic1.get(item, 0) + 1
for item in t:
    dic2[item] = dic2.get(item, 0) + 1
return dic1 == dic2

```
3.只需要使用一个hash表，前一次遍历增加值，后一次遍历减少值
最后判断hash表中的值是否为0
```angular2html
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

```angular2html
if len(s) != len(t):
    return False
for i in set(s):
    if s.count(i) != t.count(i):
        return False
return True
```
优化
```angular2html

if len(s)!=len(t):return False
tmp = set(s)
if tmp == set(t):#如果两个字符串的set相同进行深入判断
    for i in tmp:
        if s.count(i) != t.count(i): return False
    return True
return False
```

--

### 二叉树的深度优先遍历
递归实现都比较简单，也比较容易理解，不赘述
 
#### 二叉树的前序遍历 根左右

1.递归实现
```angular2html
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

```angular2html
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

--
#### 二叉树的中序遍历 左根右
1.递归实现
```angular2html
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
所以要确保能一直往最左节点找同时入栈 如果已经找到最左节点，
那么首先应当将这个元素出栈存入res中 其次应判断当前栈顶元素是是否有右孩子 将cur指向栈顶元素的右孩子
```angular2html
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
--

#### 二叉树的后序遍历 左右根
1.递归实现
```angular2html
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

```angular2html
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
        stack2.append(node)
    return stack2[::-1]
```

#### 二叉树的层序遍历
写着写着，才发现二叉树的层序遍历和我上面后序遍历是真的像
```angular2html
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
```angular2html
def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        quene,res = [root],[]
        while quene:
            cur = stack1.pop()
            if cur is not None:
                print(type(cur))#cur is Node
                #tmp = []
                #for item in cur:
                #   tmp.append(item.val)
                #res.append(tmp)
                res.append([item.val for item in cur])
                for child in cur.children:
                    stack1.append(child)
        return res
```
改进之后，这里 实际上quene每次存储的都是每一层的所有节点，
每次都将quene所有元素记录到tmp中，将所有节点合并为list之后存入res
同时，在加入的过程中，用tmp_quene记录下一层的节点值，
在遍历完上层节点后，将下层节点赋给quene
```angular2html
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


--
#### 数组中最小的k个数
1.暴力解法 对数组进行排序，返回前k个
```angular2html
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
```angular2html
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