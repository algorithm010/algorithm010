# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/15 7:42 PM

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        异位词的概念是 字符串中出现的字母都是一样的且对应字母其次数也一致
        :type s: str
        :type t: str
        :rtype: bool
        """
        #1.对这两个字符串进行排序，如果排序结果一致，说明是异位词
        #击败22%
        # return sorted(s) == sorted(t)
        #2.遍历两个字符串，检查生成的hash表是否一致
        #击败32%
        # dic1, dic2 = {}, {}
        # for item in s:
        #     dic1[item] = dic1.get(item, 0) + 1
        # for item in t:
        #     dic2[item] = dic2.get(item, 0) + 1
        # return dic1 == dic2
        #2.只需使用一个hash表 hash表记录每个字母出现的次数
        #击败58%
        #hash表的key也可以使用ord(item)-ord('a')
        # if len(s) != len(t): return False
        # hashmap = {}
        # for substr in s:
        #     if not hashmap.get(substr):
        #         hashmap[substr] = 1
        #     else:
        #         hashmap[substr] += 1
        # for substr in t:
        #     if hashmap.get(substr):
        #         hashmap[substr] -= 1
        #     else:
        #         return False
        # for value in hashmap.values():
        #     if value != 0:
        #         return False
        # return True
        #4.python中使用count函数统计出现的次数
        #击败90%
        # if len(s) != len(t):
        #     return False
        # for i in set(s):
        #     if s.count(i) != t.count(i):
        #         return False
        # return True

        #击败95%
        if len(s) != len(t): return False
        tmp = set(s)
        if tmp == set(t):#如果两个字符串的set相同进行深入判断
            for i in s:
                if s.count(i) != t.count(i): return False
            return True
        return False
        #

# leetcode submit region end(Prohibit modification and deletion)
