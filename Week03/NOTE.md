学习笔记

#### 括号生成
1.因为括号类别已经确定，可以想象为左右括号最多N个
左括号出现次数小于N即可,右括号小于左括号个数
```angular2html
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
```angular2html
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

#### 翻转二叉树
1.递归
我刚开始的想法是，考虑左右孩子节点，这个连接指向修改了就好了  
然后写的代码如下
```angular2html
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
```angular2html
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
```angular2html
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
```angular2html
if root is None: return True
#确定左子树是否符合排序二叉树，如果不满足，就返回False
if not self.isValidBST(root.left): return False
if root.val <= self.pre_val: return False#不满足左子树小于根节点
self.pre_val = root.val#记录上一个访问的节点的值
#访问右子树 # drill down
return self.isValidBST(root.right)
```
2.迭代 由于二叉搜索树的特性 中序遍历比较方便 这里就借用二叉树的中序遍历的非递归实现完成
```angular2html
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
```angular2html
if root is None: return 0
return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```
2.迭代 借助DFS思想，借助栈，每次入栈时 记录当前节点的深度  
将遍历左右孩子时，将节点和当前深度+1压入栈中
```angular2html
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

#### 二叉树的最小深度
1.递归 递归时需要弄清楚递归的结束条件
```angular2html
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
    return min(left_height,right_height)+1
```
2.借助层序遍历 不需要遍历所有节点 只需要遍历到第一个叶子节点就能返回
```angular2html
if not root: return 0
quene = [(1, root)]
while quene:
    #[3,9,20,null,null,15,7]
    depth, root = quene.pop(0)  # 保证从左往右看，如果是pop(0)，那么可能往右看的过程中返回了，而丢失了应有的最小值
    if not root.left and not root.right: return depth  # 如果此节点左右为空 返回当前depth
    if root.left: quene.append((depth + 1, root.left))
    if root.right: quene.append((depth + 1, root.right))
```

#### 二进制求和
1.进制转换后求解
```angular2html
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
```angular2html
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
```angular2html
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
```angular2html
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
