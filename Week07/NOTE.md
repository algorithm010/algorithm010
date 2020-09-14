学习笔记

#### Trie树
Trie树每个节点只存单一字符，每条路径存相对应的单词  
要实现三个方法insert、search、startwith  
```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True
```

#### 单词搜索I
判断单词是否在矩阵中  
从矩阵的任意位置出发，开始寻找  
DFS+回溯 时间复杂度为O(4MNMN)  
```python
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, board, word):
                    return True
        return False

    def dfs(self, i, j, board, word):
        if len(word) == 0: return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return  # 回溯
        tmp = board[i][j]
        board[i][j] = '#'  # 标志着已经选用过,到下一层哪怕选了 也是!=word[0],会回溯
        res = self.dfs(i + 1, j, board, word[1:]) or self.dfs(i - 1, j, board, word[1:]) \
              or self.dfs(i, j + 1, board,word[1:]) or self.dfs(i,j - 1,board,word[1:])
        board[i][j] = tmp
        return res
```

#### 单词搜索II
和上一题意思差不多，只不过这次是判断字典中的字符串是否在矩阵中，输出在矩阵中的字符串    
可以还是照上面的思路 但是又要加一层循环，所以是O(K4MNMN)，k是字典中字符串的个数  
在回溯的过程中，我们是对一个节点的四个兄弟节点判断完都不符合之后才能回溯，然后继续这样向上回溯  
但是在某个时刻 如果当前路径不是待求字符串的前缀，我们可以不用向下走了  
此时的时间复杂度是O(MN4*3^(L-1))  
从一个单元格开始，最初我们最多可以探索4个方向。  
假设每个方向都是有效的（即最坏情况），在接下来的探索中，我们最多有 3 个相邻的单元  
```python
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch,{})
            node['end'] = 0 #将所有word构建为tree树
        rows, cols = len(board), len(board[0])
        res = set()
        def dfs(i,j,root,s):
            cur = board[i][j]
            if cur not in root: return#剪枝
            root = root[cur]#下探
            if 'end' in root and root['end'] == 0:
                res.add(s+cur)#到达叶节点，加入到结果集
            board[i][j] = '@'#
            for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
                tmp_i,tmp_j = x + i, y + j
                if 0 <= tmp_i < rows and 0 <= tmp_j < cols and board[tmp_i][tmp_j]!='@':
                    dfs(tmp_i,tmp_j,root,s + cur)
            board[i][j] = cur#reverse state
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,'')
        return list(res)
```

#### 并查集 
并查集是用来判断图中是否有环的算法  
需要实现两个函数 find 和 union
```python
SIZE = 7
parent =[-1] * SIZE#-1代表指向自己，自己成环
rank = [0] * SIZE#记录当前的深度
def find(x, parent):#找到老大
    node = x
    while parent[node] != -1:
        node = parent[node]
    return node

def union(x, y):#合并两个节点
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root == y_root:#如果老大是同一人
        return
    # parent[y_root] = x_root
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[y_root] > rank[x_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1
```