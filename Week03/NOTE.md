学习笔记



#### 翻转二叉树
1.递归
我刚开始的想法是，考虑左右孩子节点，这个连接指向修改了就好了  
然后写的代码如下
```python
def invertTree(self, root: TreeNode) -> TreeNode:
    #recursive terminator
    if root is None: return
    #current process
    if root.right:
        root.left = self.invertTree(root.right)
    if root.left:
        root.right = self.invertTree(root.left)
    #drill down
    #reverse states
    return root
```
上述代码的问题在于，if root.right:执行过后，左孩子已经修改了；在想要执行if root.left:时已经是同一个指向了  
所以需要修改
```python
def invertTree(self, root: TreeNode) -> TreeNode:
    # recursive terminator
    #击败70%
    if root is None: return
    # current process
    left = self.invertTree(root.right)
    right = self.invertTree(root.left)
    root.left = left
    root.right = right
    # drill down
    # reverse states
    return root

```
2.迭代 类似层序遍历，将每一层访问到的节点存到quene中  
如果quene不为空，取出队尾元素 对于当前节点，交换左右孩子后，将其添加到quene中，继续进行判断
```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None: return None
    quene = [root]
    while quene:
        cur = quene.pop()
        cur.left, cur.right = cur.right, cur.left
        if cur.left is not None: quene.append(cur.left)
        if cur.right is not None: quene.append(cur.right)
    return root
```

#### 验证是否搜索二叉树
1.递归，判断左子树是否小于根，右子树是否大于根
```python
if root is None: return True
#确定左子树是否符合排序二叉树，如果不满足，就返回False
if not self.isValidBST(root.left): return False
if root.val <= self.pre_val: return False#不满足左子树小于根节点
self.pre_val = root.val#记录上一个访问的节点的值
#访问右子树 # drill down
return self.isValidBST(root.right)
```
2.迭代 由于二叉搜索树的特性 中序遍历比较方便 这里就借用二叉树的中序遍历的非递归实现完成
```python
stack, pre_val = [], float('-inf')
cur = root
while stack or cur is not None:
    while cur is not None:#一直往下找，到左叶节点
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    if cur.val <= pre_val: return False#判断左节点值与根节点的大小关系
    pre_val = cur.val#修改当前的根节点大小
    cur = cur.right
return True
```

#### 二叉树的最大深度
1.递归代码 这个代码我真的印象超级深
```python
if root is None: return 0
return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```
2.迭代 借助DFS思想，借助栈，每次入栈时 记录当前节点的深度  
将遍历左右孩子时，将节点和当前深度+1压入栈中
```python
if root is None: return 0
stack = [(1, root)]#栈中记录当前节点和此时的高度
depth = 0
while stack != []:
    current_depth, root = stack.pop()#这里pop(0)和pop()都可以
    if root is not None:
        depth = max(depth, current_depth)#记录当前节点的高度
        stack.append((current_depth + 1, root.left))#当前深度+1
        stack.append((current_depth + 1, root.right))
return depth
```
上述代码可以优化  
``` python
    quene, depth = [root], 0
    while quene:
        # cur_layer = []
        for _ in range(len(quene)):
            root = quene.pop(0)#要确保将这一层的元素加入到quene中
            if root.left: quene.append(root.left)
            if root.right: quene.append(root.right)
        depth += 1
    return depth
```

#### 二叉树的最小深度
最小深度是从根节点到最近叶子节点的最短路径上的节点数量  
1.递归 递归时需要弄清楚递归的结束条件
```python
def minDepth(self, root: TreeNode) -> int:
    #1.根节点为空 return 0
    #2. 左右节点为空 return 1
    #3.左节点或右节点为空 return 左/右+1
    #4.左右节点都不为空 return min(left,right)+1
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    left_height, right_height = self.minDepth(root.left),self.minDepth(root.right)
    if root.left is None or root.right is None:  return left_height+right_height+1#有一个为0
    #其余情况 返回较小值+1
    return min(left_height,right_height) + 1#+1是加的根那一层
```
2.借助层序遍历 不需要遍历所有节点 只需要遍历到第一个叶子节点就能返回
```python
if not root: return 0
quene = [(1, root)]
while quene:
    #[3,9,20,null,null,15,7]
    depth, root = quene.pop(0)  # 保证从左往右看，如果是pop()，那么可能往右看的过程中返回了，而丢失了应有的最小值
    if not root.left and not root.right: return depth  # 如果此节点左右为空 返回当前depth
    if root.left: quene.append((depth + 1, root.left))
    if root.right: quene.append((depth + 1, root.right))
```
这里和上面最大深度逻辑一致，只要提前判断子树就可以返回深度了  
``` python
if not root: return 0
quene, depth = [root], 1
while quene:
    for _ in range(len(quene)):
        root = quene.pop(0)
        if not root.left and not root.right: return depth#提前判断是否叶节点即可，由于depth是后加的，所以初值depth=1
        if root.left: quene.append(root.left)
        if root.right: quene.append(root.right)
    depth += 1
```

#### 二进制求和
1.进制转换后求解
```python
return bin(int(a, 2)+int(b, 2))[2:]
```
2. 如果不能使用加减乘除
```angular2html
#2.如果不能使用加减乘除运算，则使用位运算
x, y = int(a, 2), int(b, 2)
while y:
    res = x ^ y #无进位相加结果
    carry = (x & y) << 1#计算x+y的进位
    x, y = res, carry
return bin(x)[2:]
```


#### 单词拆分
1.动态规划 时间复杂度O(N^2),空间复杂度O(N)
```python
#动态规划 用大小为len(s)+1的数组保存转态结果
#dp[i]表示s的前i位是否能被worddict中的元素表示,最后只需要取转移数组的最后一位即可知道是否能够拆分
#如何转移呢？
#外层i从[0,len(s))，内层j[i+1,n]
        #如何从i转移到j？ 如果dp[i]=True并且s[i:j]在worddict中，即可转移
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if dp[i]==True and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]
```
2.备忘录回溯
```python
#备忘录回溯
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    import functools
    @functools.lru_cache
    def backtrace(s):
        if not s: return True#s已经考察结束
        res = False
        for i in range(1, len(s)+1):#
            if s[:i] in wordDict:
                res = backtrace(s[i:]) or res#记录递归过程中的res
        return res#最后返回的相当于是dp[-1]or(dp[-2]or(dp[-n])) 其实只用看最后一层的res即可
    return backtrace(s)
```

#### 最接近的三数之和
1.枚举所有组合 枚举过程中 使用双指针优化 枚举过程  
这里最后是要返回最接近target的三个数的和 min_closer 用来记录最接近的三数之和  
首先对数组排序 然后 写出标准的三指针遍历模式 对于left<right 记录当前的三数之和   
如果当前的三数之和与target差值的绝对值 小于 abs(min_closer-tmp)，就将min_closer=tmp    
如果小于target，left+1 如果大于target，right-1 如果=target就返回这个三数之和  
遍历结束之后 没有返回 说明没有=target的组合 那么就返回记录的最接近的三数之和min_closer  
```python
def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()  # 先排序
    # [-4,-1,1,2],1
    min_closer = float('inf')
    for i in range(len(nums) - 2):  # 为双指针留出位置
        if i > 0 and nums[i] == nums[i - 1]:  # 保证前后两个数字不一，因为只有一组解
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            tmp = nums[i] + nums[left] + nums[right]  # 先记录当前遍历得到的三数之和
            if abs(min_closer - target) > abs(tmp - target):
                min_closer = tmp
            # min_closer = min(abs(target-tmp),min_closer)
            if tmp < target:  # 如果还没有找到相等的 ，j右移
                left = left + 1
                # cur_diff = abs()
            elif tmp > target:  # 如果找着找着 大于target了，就需要和之前记录的min_diff比较
                right = right - 1
            else:  # tmp==target:
                return min_closer
    return min_closer
```

#### 最长回文子串
1.暴力解法
遍历出所有长度的子串，判断它是否是回文串，从结果中挑出最长的返回  时间复杂度是O(N^3)
```python
def longestPalindrome(self, s: str) -> str:
    res,max_length = '',0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            cur_string = s[i:j]
            if self.isPalidrome(cur_string) and len(cur_string)>max_length:
                res = cur_string
                max_length = max(max_length,len(res))
    return res

def isPalidrome(self,cur_string):
    #判断是否回文字符
    left,right = 0,len(cur_string)-1
    while left<right:
        if cur_string[left]!=cur_string[right]:
            return False
        left,right = left+1,right-1
    return True
```
2.动态规划
动态规划是指 如果这一刻的状态是可以由其他时刻的状态推导出来，那么我们可以记录该时刻的状态以推导此刻的状态  
```python
#首先 长度为0、1的字符串 它是回文串
#长度=2，判断左右是否相同
#对于strs[i,j]而言它是否是回文串 取决于它内缩2位的字符串是否是回文串同时还要判断其边界是否相同，=2也可划归此类    
#动态规划的思想就是 每一次的状态都是可以由其他时刻的状态导出的  
#而通常我们在做题时，总会借助额外的空间，这个空间的维度与我们的状态有关，
#比如此时要记录i,j组合状态，就需要二维数组记录
#对于上面长度为0，1的字符串
def longestPalindrome(self, s: str) -> str:
    size = len(s)
    dp = [[False] * size for _ in range(size)]  # 为什么是一个二维数组
    res = ""
    # 枚举子串的长度 l+1
    for L in range(size):
        # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
        for i in range(size):
            j = i + L
            if j >= len(s):
                break
            if L == 0:  # 如果当前字符长度为0
                dp[i][j] = True#i==j，为True
            elif L == 1:  # 如果当前字符长度为1
                dp[i][j] = (s[i] == s[j])
            else:  #
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and L + 1 > len(res):
                res = s[i:j + 1]
    return res
```
#### 序列话和反序列化二叉树
遍历二叉树有深度和广度，但是由于要重建二叉树，我们普通的遍历结果是连在一起的，无法确定None节点在哪里，  
所以如果想要用一次遍历的结果推导出其二叉树的构型 需要为叶节点的孩子打上标记
1.BFS 层序遍历实现
 - 1 序列化 层序遍历的二叉树
 ```python
def serialize(self, root):#层序遍历中使用deque是最简单的
    #手写一个二叉树的层寻遍历
    if not root: return []
    dquene,res = [root],''
    while dquene:
        cur = dquene.pop(0)#使用了双端队列
        if cur !=  None:
            res += str(cur.val)+','
            dquene.append(cur.left)
            dquene.append(cur.right)           
        else:
            res += '#,'#标识None
        return res
```
 - 2 重建时，如果遍历到的元素是#，那我们就不对它进行处理
 ```python
def deserialize(self, data):
    if not data: return None
    data = data.split(',')
    root = TreeNode(data.pop(0))
    dquene = [root]
    while dquene:
        cur = dquene.pop(0)
        if data:
            cur_left = data.pop(0)
            if cur_left != '#':#反序列化时，如果节点值为#就不处理
                cur.left = TreeNode(cur_left)
                dquene.append(cur.left)
        # if data:
            cur_right = data.pop(0)
            if cur_right != '#':
                cur.right = TreeNode(cur_right)
                dquene.append(cur.right)
    return root
```

2.前序遍历 递归解
 - 1 序列化 前序遍历
```python
def serialize(self, root):
    #手写一个二叉树的层寻遍历
    if root == None: return '#,'
    leftserilized = self.serialize(root.left)
    rightserilized = self.serialize(root.right)
    return str(root.val) + ',' + leftserilized + rightserilized
```
 - 2 反序列化
```python
def deserialize(self, data):
    data = data.split(',')
    root = self.deserializeCore(data)
    return root

def deserializeCore(self,data):
    root_val = data.pop(0)
    if root_val == '#': return None
    root = TreeNode(root_val)
    root.left = self.deserializeCore(data)
    root.right = self.deserializeCore(data)
    return root
```

#### 二叉树的最近公共祖先
1.递归
class Solution:
```python
#1.递归 分析出找到最近公共祖先节点的情形，如果p，q由同一祖先节点 则p、q要么位于某棵树的左右子树
    #要么在同一棵树上，在同一棵树上又有 p或q为根 另外存在p或q在其左右子树中
    res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root,p,q)
        return self.res

    def dfs(self,root,p,q):
        # recursive terminator
        if root is None: return False
        #current process
        #drill down
        root_left = self.dfs(root.left,q,p)#判断这颗树的子树中是否含有q节点或者q节点
        root_right = self.dfs(root.right,p,q)
        #要判断p、q的最近公共祖先，我们从根节点开始寻找，查探root的左子树和右子树是否包含q节点或p节点，此时最近公共最先就是root；另外的，如果p或q为子树根节点，且p或q处在这棵子树下面，则最进公共祖先就是p或q节点
        if root_left and root_right or ((root.val==p.val or root.val==q.val) and(root_left or root_right) ):#对于5，1这种情况，这是后就要返回p为true给上层递归
            self.res = root#那么就返回当前树的根节点
        #reverse states
        return root_left or root_right or(root.val==p.val or root.val==q.val)
```
写的更简洁一点
```python
def lowestCommonAncestor(self, root, p, q):
    if not root or p==root or q==root:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
```

2.记录父节点
```python
class Solution:
    # ，然后我们就可以利用节点的父节点信息从p结点开始不断往上跳，并记录已经访问过的节点，再从q节点开始不断往上跳，如果碰到已经访问过的节点，那么这个节点就是我们要找的最近公共祖先。
    all_parents = {}
    p_parents = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.all_parents[root.val] = None
        self.dfs(root)  # 用哈希表存储所有节点的父节点
        # 在all_parents找p的根节点，并且记录找到的父节点
        while p != None:
            self.p_parents[p.val] = True
            p = self.all_parents.get(p.val)
        while q != None:  # 因为p、q是必有公共父节点的，所以一定能在p_parents里面找到父节点
            if self.p_parents.get(q.val):  # 如果如果在p的parent中找到
                return q
            q = self.all_parents.get(q.val)  # 如果没找到，说明q可能还要向上一层才能找到
        return None

    def dfs(self, root):  # 从root开始遍历子节点 记录子节点值作为key，值为root节点
        if root.left is not None:
            self.all_parents[root.left.val] = root
            self.dfs(root.left)
        if root.right is not None:
            self.all_parents[root.right.val] = root
        self.dfs(root.right)
```

#### 根据二叉树的前中序列重建二叉树
手动模拟根据二叉树的前中序列生成二叉树的过程，不难发现每次都是先确定根节点，以根节点划分出左右子树  
对应到两个序列，递归的进行确定根节点，左右子树序列  
所以我们在重建时，先确定根节点、然后为其分配左右子树，
处理左右子树时，先确定并对应其前中序列，进行相同的处理  
```python
def buildTree(self, pre: List[int], inorder: List[int]) -> TreeNode:
    if not pre or not inorder:
        return None
    root = TreeNode(pre[0])
    index = inorder.index(root.val)#记录root在中序序列中的位置
    root.left = self.buildTree(pre[1:index+1],inorder[:index])
    root.right = self.buildTree(pre[index+1:],inorder[index+1:])
    return root
```


#### 删除未排序链表中的重复元素
1.使用set实现存储未重复元素，然后重建 (超时)尽管时间复杂度是O(N)，但是相当于遍历了两次
```python
if head is None or head.next is None: return head
    once = set()
    while head is not None:
        if head.val not in once:
            once.add(head.val)
            head = head.next         
    head = pre = ListNode(None)
    while once:
        head.next = ListNode(once.pop())
        head = head.next
    return pre.next
```
可以知道，如果当前元素已经出现过，那么如果遍历时记录了前一个指针，那么可以直接删除掉这个节点元素
```python
if not head: return head
    once = {head.val}
    pre = head
    while head.next:#如果有下一个节点
        cur = head.next
        if not cur.val in once:
            once.add(cur.val)
            head = head.next
        else:#如果这个元素已经出现，那就直接删除掉
            head.next = head.next.next
    return pre
```

#### 括号生成
1.因为括号类别已经确定，可以想象为左右括号最多N个
左括号出现次数小于N即可,右括号小于左括号个数
```python
def generateParenthesis(self,n):
    result = []
    self._generate_parenthesis(0, 0, n, '',result)
    return result

def _generate_parenthesis(self, left, right, n, res, result):
    # recursive terminator
    if left == n and right == n:
        result.append(res)
        return
    # current process
    if left < n: self._generate_parenthesis(left + 1, right, n, res + '(', result)
    if left > right: self._generate_parenthesis(left, right + 1, n, res + ')', result)

    # drill down

    # reverse state
```
上面这种解法，由于最后要返回res，所以在递归时传入的参数较多，可以简化一下
```python
def generateParenthesis(self,n):
    result = []
    def _generate_parenthesis( left, right, n, res):
        # recursive terminator
        if left == n and right == n:
            result.append(res)
            return
        # current process
        if left < n: _generate_parenthesis(left + 1, right, n, res + '(')
        if left > right: _generate_parenthesis(left, right + 1, n, res + ')')
    _generate_parenthesis(0, 0, n, '')
    return result
```

#### 组合
碰到组合、全排列、括号生成这种打印类的题，一般都是 回溯算法，回溯算法有一个基本模板：
```python
def backtracing(路径,可选路径)：
    #触发结束条件
    #for i in range():
        #处理不符合条件的
        #执行当前选择 路径+，可选路径-
        #进入下一层决策
        #进行有必要的撤销选择以进行回溯

```

```python
def combine(self, n, k):
    def backtracing(first=1, tmp=[]):
        #触发结束条件
        if len(tmp) == k:  # 如果当前元素 已经有k个，就将它加入res中
            res.append(tmp[:])
        for i in range(first, n + 1):  # 如果当前元素个数小于k，则加入cur中
            # 做选择
            tmp.append(i)
            # 进入下一层决策
            backtracing(i + 1, tmp)
            # 撤销刚才的选择  
            tmp.pop()  
    res = []
    backtracing()
    return res
```


#### 组合II

#### 全排列
```python
def permute(self, nums: List[int]) -> List[List[int]]:
    def backtrace(nums, tmp):
        #触发结束条件
        if not nums:
            res.append(tmp[:])
        for i in range(len(nums)):
            #排除不合法或已存在的
            if nums[i] in tmp: continue
            #做选择 修改已选路径和能选择的路径
            #进入下一次决策、回溯之前的决策
            backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])#修改选择项和路径
    res = []
    backtrace(nums, [])
    return res
```

#### 全排列II
```python
class SolutionII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums,tmp):
            if len(tmp) == size:
                res.append(tmp[:])
            for i in range(len(nums)):
                backtrace(nums[:i]+nums[i+1:],tmp+[nums[i]])
        res, size = [], len(nums)
        backtrace(nums,[])
        return res
```
上面在判重的时候，是在写入res时手动遍历判重，其实可以直接用set记录中间结果  
```python
def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrace(nums, tmp):
        if not nums:
            res.append(tmp[:])
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited: continue            
            visited.add(nums[i])
            backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])#修改选择项和路径

    res = []
    backtrace(nums, [])
    return res
```

#### Pow(x,n)
1.遍历n次，时间复杂度O(N)
```angular2html
if n==0: return 1
flag=False if n< 0 else True
times,res = abs(n),1
while times>0:
    res *= x
    times -= 1
return res if flag else 1/res
```
递归形式如下 但是都超出时间限制    
```angular2html
if n == 1: return x
if n < 0:
    return 1 / self.myPow(x, -n)
return self.myPow(x, n // 2) * self.myPow(x, n - n // 2)
```

2.我们可以将这个问题的时间复杂度缩减到O(logN),求x的N次方 我们可以化简为计算两次x的N/2次（判断奇偶）
```angular2html
if n == 1: return x
if n < 0:
    return 1 / self.myPow(x, -n)
return self.myPow(x*x, n // 2) if n%2==0 else x*self.myPow(x, n-1)
```

#### 子集
1.递归
```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for num in nums:
        res += [tmp + [num] for tmp in res]
    return res
```
2.回溯
```python
def subsets(self, nums: List[int]) -> List[List[int]]:    
    def backtrack(first=0, tmp=[]):
    #处理结束条件
    if len(tmp) == k:
        res.append(tmp[:])
    for i in range(first, size):
        #选择
        tmp.append(nums[i])
        # print(curr)
        #下一层决策
        backtrack(i + 1, tmp)
                tmp.pop()
    res = []
    size = len(nums)
    for k in range(size + 1):
        backtrack()
    return res

```
3.位运算
```python
def subsets(self, nums: List[int]) -> List[List[int]]:    
    size = len(nums)
    res = []
    for i in range(2 ** size, 2 ** (size + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        # append subset corresponding to that bitmask
        res.append([nums[j] for j in range(size) if bitmask[j] == '1'])
    return res
```

#### 字符串相加
手动模拟数字进位加法，如果两个数长度不一致，就在将其作为0处理
```python
def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    #1.转数字计算
    # return str(int(num1)+int(num2))
    # 2.手动模拟加法运算
    res = ''
    i, j, carry = len(num1) - 1,len(num2) - 1, 0
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        tmp = n1 + n2 + carry
        carry = tmp // 10
        res = str(tmp % 10) + res
        i, j = i - 1, j - 1
    return '1' + res if carry else res
```

#### 长度最小的子数组
1.枚举出长度为1,2,3...的数组，查看其值是否大于s，如果大于则可以直接返回 此时的枚举长度 但是时间复杂度高 O(N^2)
```python
def minSubArrayLen(self, s, nums):
# 1. 穷举 超出时间限制
    for i in range(1, len(nums) + 1):
        # 长度为1，2，3，穷举可能的解，找到则返回
        for j in range(len(nums) - i + 1):
            if sum(nums[j:i + j]) >= s: return i
    return 0
```
2.穷举的过程中，有很多不必要的开销，比如每次指定长度的窗口，但是大多数窗口都是无效的  
就像窗口为1时 计算和之后 判断了一次 如果不符合规定 就往后挪了一位 不符合需要继续后移  
窗口值为2时，又计算了前面的过程  
所以我们可以使用双指针 来界定是否是最短子数组
双指针开始时指向 数组头 如果当前窗口和 小于s，end右移 以达到期望的s，如果此时已经到达s，记录下当前的窗口值  
将当前窗口往右移动 继续判断窗口值与s的关系，如果小了，就右移end；如果还是大于s，窗口继续右移
```python
def minSubArrayLen(self, s, nums):
    if not nums: return 0
    size, res = len(nums), len(nums) + 1
    start, end = 0, 0
    tmp = 0  # 记录窗口和
    while end < size:
        tmp = tmp + nums[end]
        while tmp >= s:  # 如果当前窗口和值大于s,收缩窗口
            res = min(res, end - start + 1)
            tmp = tmp - nums[start]
            start = start + 1
        end = end + 1  # 窗口扩张
    return 0 if end == size + 1 else res
```
