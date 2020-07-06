class Solution:
    from typing import List
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(coins, amount, i, count, res):  # 如果当前coin用完了，就换面值更小的
            if amount == 0: return min(count, res)
            if i == -1: return res#已经遍历完所有coin
            #current layer
            multiple = amount//coins[i]
            while multiple >= 0 and multiple + count < res:#这里往往是一个循环要么是for，要么是while
                res = dfs(coins,amount-multiple*coins[i], i-1, count+multiple, res)#count用来记录上一层的组合数
                multiple -= 1
            return res # 回溯结束
        if amount == 0: return 0
        coins.sort()
        result = dfs(coins, amount, len(coins)-1, 0, float('inf'))
        return result if result != float('inf') else -1

    #动态规划
    def coinChangeI(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for cur in range(amount + 1):
            for coin in coins:  # 往当前位置的前[coins]个位置看，取最小的+1
                if cur >= coin:  # 如果cur<coin，没法拼凑
                    dp[cur] = min(dp[cur - coin] + 1, dp[cur])
        return dp[amount] if dp[amount] != float('inf') else -1



s = Solution()
coins = [1, 2, 5]
amount = 11
res = s.coinChange(coins,amount)
print(res)
