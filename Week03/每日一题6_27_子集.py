from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # for num in nums:
        #     res += [tmp + [num] for tmp in res]
        # return res
        # def backtrack(first=0, tmp=[]):
        #     #处理结束条件
        #     if len(tmp) == k:
        #         res.append(tmp[:])
        #     for i in range(first, size):
        #         #选择
        #         tmp.append(nums[i])
        #         # print(curr)
        #         #下一层决策
        #         backtrack(i + 1, tmp)
        #         tmp.pop()
        #
        # res = []
        # size = len(nums)
        # for k in range(size + 1):
        #     backtrack()
        # return res

        size = len(nums)
        res = []
        for i in range(2 ** size, 2 ** (size + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            res.append([nums[j] for j in range(size) if bitmask[j] == '1'])
        return res



s = Solution()
res = s.subsets([1,2,3])
print(res)