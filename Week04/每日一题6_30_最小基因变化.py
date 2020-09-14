# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/30 12:19 AM

# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。
#
#  注意:
#
#
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
#  所有的目标基因序列必须是合法的。
#  假定起始基因序列与目标基因序列是不一样的。
#
#
#  示例 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# 返回值: 1
#
#
#  示例 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# 返回值: 2
#
#
#  示例 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# 返回值: 3
#
#


# leetcode submit region begin(Prohibit modification and deletion)


# 1.BFS 所谓BFS就是类似二叉树BFS我们使用deque的非递归实现
import collections
def isChangeOnce(cur,next):#时间复杂度是O(K),K是bank中字符的长度
    changes = 0
    for i in range(len(next)):
        if next[i]==cur[i]:
            changes = changes + 1
    return changes == 1#但是可以不必要全部遍历完，大于1的时候就可以直接返回

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        对于每一个节点都要去找与它只相差一个的元素list，然后与这个list中所有元素进行比较，然后继续去找相差1的元素
        时间复杂度是O(N)*O(N)*O(K)*
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # quene = collections.deque()
        # quene.append((start,start,0))#cur,pre,steps
        # while quene:
        #     cur,pre,steps = quene.popleft()
        #     if cur == end:
        #         return steps
        #     for gene in bank:#bank长度
        #         if isChangeOnce(cur,gene) and gene != pre:
        #             quene.append((gene,cur,steps+1))
        # return -1
        queue = []
        queue.append((start, 0))
        visited = set(bank)
        while queue:
            cur, step = queue.pop(0)
            if cur == end:
                return step
            for i in range(len(cur)):
                for c in "AGCT":  #
                    mutation = cur[:i] + c + cur[i + 1:]  # 列举出所有可能的变化为1的基因串
                    if mutation in visited:
                        visited.remove(mutation)
                        queue.append((mutation, step + 1))
        return -1



# 2.DFS 回溯
from typing import List
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


# leetcode submit region end(Prohibit modification and deletion)
