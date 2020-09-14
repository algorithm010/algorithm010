# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/6/25 8:40 AM

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
#  说明：
#
#
#  拆分时可以重复使用字典中的单词。
#  你可以假设字典中没有重复的单词。
#
#
#  示例 1：
#
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
#
#  示例 2：
#
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#
#
#  示例 3：
#
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #动态规划 用大小为len(s)+1的数组保存转态结果
        #dp[i]表示s的前i位是否能被worddict中的元素表示,最后只需要取转移数组的最后一位即可知道是否能够拆分
        #如何转移呢？
        #外层i从[0,len(s))，内层j[i+1,n]
        #如何从i转移到j？ 如果dp[i]=True并且s[i:j]在worddict中，即可转移
        # dp = [False for _ in range(len(s)+1)]
        # dp[0] = True
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)+1):
        #         if dp[i]==True and s[i:j] in wordDict:
        #             dp[j] = True
        # return dp[-1]

        #备忘录回溯
        # import functools
        # @functools.lru_cache
        # def backtrace(s):
        #     if not s: return True#s已经考察结束
        #     res = False
        #     for i in range(1, len(s)+1):#
        #         if s[:i] in wordDict:
        #             res = backtrace(s[i:]) or res#记录递归过程中的res
        #     return res#最后返回的相当于是dp[-1]or(dp[-2]or(dp[-n])) 其实只用看最后一层的res即可
        # return backtrace(s)

        while s:
            for item in wordDict:
                s = s.replace(item, '')
            return False
        return s == ''
    # leetcode submit region end(Prohibit modification and deletion)

# strs = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
strs = "abcd"
wordDict = ["a","abc","b","cd"]
s = Solution()
res = s.wordBreak(strs,wordDict)
print(res)