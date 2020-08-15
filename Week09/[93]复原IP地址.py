# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/14 10:28 PM

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        if size < 4 or size > 12:
            return []
        path = []
        res = []
        self.__dfs(s, size, 0, 0, path, res)
        return res

    def __dfs(self, s, size, split_times, begin, path, res):
        if begin == size:
            if split_times == 4:
                res.append('.'.join(path))
            return
        # 如果剩余长度不够划分、如果剩余长度太长
        if size - begin < (4 - split_times) or size - begin > 3 * (4 - split_times):
            return
        for i in range(3):
            if begin + i >= size:
                break
            ip_segment = self.__judge_if_ip_segment(s, begin, begin + i)
            if ip_segment != -1:
                path.append(str(ip_segment))
                self.__dfs(s, size, split_times + 1, begin + i + 1, path, res)
                path.pop()

    def __judge_if_ip_segment(self, s, left, right):
        size = right - left + 1
        if size > 1 and s[left] == '0':
            return -1
        res = int(s[left:right + 1])
        if res > 255:
            return - 1
        return res


class SolutionI:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 定义查找符合条件的数字个数
        def _dfs(start, path):
            # recursion terminator
            # 如果ip地址已4位，但字符串没用尽，不符合题目意思
            if len(path) == 4 and start < len(s)-1:
                return
            # 什么时候加入到res中？？？ 当整个字符串已经遍历完成的时候
            if start>=len(s):
                if len(path) == 4:
                    res.append('.'.join(path))
                return
            # 如果当前位为0，不能扩展
            # 下面的层数返回结果，此时0不能向右扩展，只能向上return
            if s[start] == '0':
                path.append(s[start])
                _dfs(start+1, path)
                path.pop()
                return
            for i in range(start,len(s)):
                if 0 <= int(s[start:i+1]) <= 255:
                    path.append(s[start:i+1])
                    _dfs(i+1,path)
                    path.pop()
                else:
                    break #后面的不用再继续判断
        res = []
        _dfs(0,[])
        return res

s = Solution()
res = s.restoreIpAddresses("25525511135")
print(res)
