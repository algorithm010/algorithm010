# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 9:40 PM

# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #击败74%
        # from collections import defaultdict
        # ans = defaultdict(list)
        # #根据异位词分组 {('a','b','c'):['abc']}
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return list(ans.values())

        #击败36%
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return list(ans.values())

        #击败50%

        # d = {}
        # for w in sorted(strs):
        #     key = tuple(sorted(w))
        #     d[key] = d.get(key, []) + [w]
        # return list(d.values())

        dic = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in dic:
                dic[s].append(string)
            else:
                dic[s] = [string]
        # return [x for x in dic.values()]#击败94%
        return [dic[x] for x in dic]#击败97%


# leetcode submit region end(Prohibit modification and deletion)