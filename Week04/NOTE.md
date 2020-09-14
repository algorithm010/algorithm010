学习笔记

#### 二叉树的层序遍历
1.BFS 与一般的层序遍历相比 只是要求同一层的元素放在同一个[]中 需要对之前的模板进行改造
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 由于题目限制了最后打印输出格式每一层节点放在[]中，所以需要对普通的层序遍历进行调整
    # 在while quene循环中加入一个cur_layer记录当前层的节点以确保每次都能将该层的元素加入
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        quene,res = [root],[]
        while quene:
            cur_layer = []
            for _ in range(len(quene)):#确保将每一层的元素都加入cur_layer
                cur = quene.pop(0)
                if cur.left: quene.append(cur.left)
                if cur.right: quene.append(cur.right)
                cur_layer.append(cur.val)
            res.append(cur_layer)
        return res
```
2.DFS既然能够遍历整树的所有节点，如果需要按模板输出，需要在递归过程中记录当前树的深度，然后将该节点加入到res的对应部分
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #如果用DFS做，当然也可以得到想要的结果，只是要注意的是，遍历过程中，需要记录该节点的深度
        # 以便将它加入到res对应下标的位置
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        # recursion terminator
        if not root: return
        #process current level
        if len(res) == level: res.append([])#在开始遍历时，生成一个[]位置，4接收参数
        res[level].append(root.val)
        #drill down
        if root.left: self.dfs(root.left, level + 1, res)
        if root.right: self.dfs(root.right, level + 1, res)
```

#### 最小基因变化
1.BFS
```python
# 1.BFS 所谓BFS就是类似二叉树BFS我们使用deque的非递归实现
import collections
def isChangeOnce(cur,next):
    changes = 0
    for i in range(len(next)):
        if next[i]==cur[i]:
            changes = changes + 1
    return changes == 1#但是可以不必要全部遍历完，大于1的时候就可以直接返回

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        quene = collections.deque()
        quene.append((start,start,0))#cur,pre,steps
        while quene:
            cur,pre,steps = quene.popleft()
            if cur == end:
                return steps
            for gene in bank:
                if isChangeOnce(cur,gene) and gene != pre:
                    quene.append((gene,cur,steps+1))
        return -1
```

2.DFS 回溯法
从bank中挑选出于cur只有一个bit差异且之前没有访问过的元素，先将其加入visited，继续判断此时的cur是否与target相同
```python
rom typing import List
class SolutionI:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set()
        self.res = float('inf')
        if end not in bank: return -1
        def dfs(cur, step):
            # recursion terminator
            if cur == end:
                self.res = min(self.res, step)
                return
            #current level process
            for next in bank:
                if next not in visited and isChangeOnce(cur, next):
                    visited.add(next)
                    # drill down
                    dfs(next, step+1)
                    # reverse state
                    visited.remove(next)
        visited.add(start)
        dfs(start, 0)
        return self.res if self.res < float('inf') else -1
```

#### 每个树行的最大值
```python
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 1. 思想比较简单 在二叉树的层序遍历的基础上 对每一列表求最大值后返回
        # 2. 当然也可以在遍历过程中记录每一层的最大值
        if not root: return []
        quene, res = [root], []
        while quene:
            cur_layer = []
            # layer_max = float('-inf')
            for _ in range(len(quene)):
                cur = quene.pop(0)
                if cur.left: quene.append(cur.left)
                if cur.right: quene.append(cur.right)
                # layer_max = max(layer_max, cur.val)
                cur_layer.append(cur.val)
            res.append(cur_layer)
            # res.append(layer_max)
        return [max(item) for item in res]
        # return res
```
其中，如果以后再遇到这样的判别  
`if not root: return []`后面接`while`循环，就直接使用如下形式  
```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # if not root: return []
        quene, res = [root], []
        while any(quene):
            # cur_layer = []
            layer_max = float('-inf')
            for _ in range(len(quene)):
                cur = quene.pop(0)
                if cur.left: quene.append(cur.left)
                if cur.right: quene.append(cur.right)
                layer_max = max(layer_max,cur.val)
                # cur_layer.append(cur.val)
            # res.append(cur_layer)
            res.append(layer_max)
        # return [max(item) for item in res]
        return res
```
最后给一段极简python代码  
```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes
```


#### 两个栈实现队列
主要是要考虑从队首删除元素的情形
```python
class CQueue(object):
    def __init__(self):
        self.in_stack, self.out_stack = [],[]

    def appendTail(self, value):
        self.in_stack.append(value)

    def deleteHead(self):
        """
        删除的时候有几点要考虑，
        1.如果out_stack中有元素，说明是上一次删除没有删除完的，最优先删除
        2.如果out_stack中元素全部删除后，in_stack中没有元素，则无法删除返回-1
        3.如果in_stack中有元素，将其全部转移到out_stack中，返回pop()值
        """
        if self.out_stack: return self.out_stack.pop()
        if not self.in_stack: return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
```


#### 单词接龙

#### 岛屿数量

#### 岛屿最大面积

#### 岛屿周长

#### 买卖股票的最佳时机I

#### 买卖股票的最佳时机II

#### 有序矩阵中的第K小的值
1.暴力法 时间复杂度O(N^2)，空间复杂度O(N^2)
```python
def kthSmallestI(self, matrix: List[List[int]], k: int) -> int:
    # 1.暴力法 时间复杂度O(N^2) 空间复杂度为O(N^2)
    tmp = [x for item in matrix for x in item]
    tmp.sort()
    return tmp[-(len(tmp) - k + 1)]
```
2.借助小根堆 时间复杂度O(klogN)，空间复杂度O(N)
```python
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    size = len(matrix)
    pq = [(matrix[i][0],i,0) for i in range(size)]# 维护一个最小元素队列 (i,0) means location
    heapq.heapify(pq)
    for i in range(k-1):#第k次pop的元素直接返回
        num, row, col = heapq.heappop(pq)
        if col != size - 1:
            heapq.heappush(pq,(matrix[row][col+1],row,col+1))#如果某行没有全部删除，将当前值右边的元素如堆
    # now time = k
    return heapq.heappop(pq)[0]
```
3.双指针 时间复杂度O(Nlog(max-min))，空间复杂度O(1)
```python
def kthSmallestII(self, matrix: List[List[int]], k: int) -> int:
    #双指针 时间复杂度O(Nlog(max-min))
    # n次双指针，每次判断矩阵左侧小于num的数的个数，大于k个则右指针已动到mid
    rows, cols = len(matrix), len(matrix[0])
    def check(num):
        i, j, count = rows - 1, 0, 0
        while i >= 0 and j < cols:
            if matrix[i][j] <= num:
                count = count + i + 1  # 一竖行都小于
                j = j + 1
            else:  # 如果大于num，这一层没有比num小的了
                i = i - 1
        return count >= k

    left_up, right_down = matrix[0][0], matrix[rows - 1][cols - 1]
    while left_up < right_down:
        mid = (left_up + right_down) // 2
        if check(mid):
            right_down = mid  # 左边有大于k个数，那么第k小的数肯定在左边
        else:  # 左边没有k个数
            left_up = mid + 1
    return left_up
```
