# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/30 1:18 AM

# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
#
#
#  每次转换只能改变一个字母。
#  转换过程中的中间单词必须是字典中的单词。
#
#
#  说明:
#
#
#  如果不存在这样的转换序列，返回 0。
#  所有单词具有相同的长度。
#  所有单词只由小写字母组成。
#  字典中不存在重复的单词。
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
#  示例 1:
#
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#
#
#  示例 2:
#
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
def isChangeOnce(cur, pre):
    changes = 0
    for i in range(len(cur)):
        if cur[i] != pre[i]:
            changes += 1
        if changes > 1: return False
    return True

from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs，用deque实现，就不用递归
        quene = [(beginWord, beginWord, 0, [beginWord])]  # cur,pre,steps,path
        while quene:
            cur, pre, steps,path = quene.pop(0)
            if cur == endWord:
                return len(path)
            for word in wordList:
                if isChangeOnce(word, cur) and word != pre:
                    quene.append((word, cur, steps + 1, path+[word]))
        return 0  # 不存在这样的转换序列

# leetcode submit region end(Prohibit modification and deletion)


from collections import defaultdict
class SolutionI(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        size = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:#M
            for i in range(size):#N
                #'*ot': ['hot', 'dot', 'lot']
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(size):#遍历当前节点可能的one_differ类型
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                #确定one_differ类型，并查探可能的下一个节点
                for word in all_combo_dict[intermediate_word]:
                    #如果这个节点就是最后节点，返回
                    if word == endWord:
                        return level + 1
                    #如果不是最后节点，就将它作为当前节点，向后探查
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                #将已经访问过的'*ot': ['hot', 'dot', 'lot']这种构型 删除掉
                all_combo_dict[intermediate_word] = []
        return 0

# from collections import defaultdict
class SolutionII(object):
    def __init__(self):
        self.size = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.size):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.size = len(beginWord)
        for word in wordList:
            for i in range(self.size):
                #'*ot': ['hot', 'dot', 'lot']
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        # Queues for birdirectional BFS
        queue_begin = [(beginWord, 1)] # BFS starting from beginWord
        queue_end = [(endWord, 1)] # BFS starting from endWord
        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        res = None
        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:
            # One hop from begin word
            res = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if res:
                return res
            # One hop from end word
            res = self.visitWordNode(queue_end, visited_end, visited_begin)
            if res:
                return res

        return 0




# beginWord = "hot"
beginWord = "hit"
# endWord = "dog"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dog","dot"]

# s = Solution()
# res = s.ladderLength(beginWord,endWord,wordList)
# print(res)

from collections import defaultdict
ddict = defaultdict(list)
for word in wordList:#M
    for i in range(3):#N
        # Key is the generic word
        # Value is a list of words which have the same intermediate generic word.
        ddict[word[:i] + "*" + word[i+1:]].append(word)

print(ddict)