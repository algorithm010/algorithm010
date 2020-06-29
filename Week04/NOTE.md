学习笔记

#### 二叉树的层序遍历
1.BFS 与一般的层序遍历相比 只是要求同一层的元素放在同一个[]中 需要对之前的模板进行改造
```angular2html
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
```angular2html
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
```angular2html
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
```angular2html
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