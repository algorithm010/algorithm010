# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 9:40 PM

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

