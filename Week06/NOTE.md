学习笔记

#### 三角形的最小路径和
1. 分治 | 递归模板  
每次只能走它下一层的左和右，那么自然想到分治算法 F[i,j] = min(F[i+1,j],F[i+1,j+1])+a[i,j]  
写的过程中，就是递归的模板嘛 这种算法时间复杂度是O(2^N)，没通过，加上缓存@lru_cache  
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 分治 递归模板
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j):
            #terminator 
            if i == size-1: return triangle[i][j]
            left = dfs(i+1,j)#加左边的值
            right = dfs(i+1,j+1)
            min_val = min(left, right) + triangle[i][j]
            return min_val
        size = len(triangle)
        return dfs(0,0)
```
2.DP  
DP过程：  
1) opt subproblem,这个分治算法已经帮我们解决了  
2) DP Array,合理定义DP数组的含义  
3）DP transfer equal,写出状态转移方程  
DP通常由两种，top-down和bottom-up  
还是按照分治思想，我们采用top-down的思想
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2.top-down
        dp = triangle
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] += triangle[i-1][j-1]
                else:
                    dp[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(dp[-1])
```
可以看到上述top-down代码中有几个分支判断，这是由于能走的路径只是下三角，要考虑数组越界的情形。  
其次，上述的dp我们只是引用了，其实可以直接复用原数组  
3.bottom-up 空间复杂度只有O(N)了
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
```
4.复用原数组 节省空间
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]) 
        return triangle[0][0]
```

#### 最大子序和
由于数组中有可能存在的赋负数，所以在累加的时候，如果f(i-1)+nums[i] < nums[i]，就要丢弃前面f(i-1)的和了  
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0], max_val = nums[0], nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],0) + nums[i]
            # max_val = max(dp[i], max_val)
        return max(dp)
        # return max_val
```
当然，这里我们也可以复用原数组  
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1], 0) + nums[i]
        return max(nums)
```

#### 乘积最大的子数组
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp_min, dp_max = [0] * len(nums), [0] * len(nums)  # dp_max记录正负交替乘法中的最大值
        dp_min[0], dp_max[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                # 如果此时nums[i]大于0，如果之前是正数，那就乘上，如果是负数，那此时的最大值为此时的值
                dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i])
                # 此时原本小于0，最小值就应该乘上nums[i]；如果原本大于0，那最小的就应该是此时的值
                dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i])
            else:  # 此时nums[i]小于0
                # 如果原本dp_min小于0，它乘上num可能是最大值；如果原来是正值，(+值*负值和负值) 中要求大值
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res
```
上面的代码看上去有些冗余，考虑是否能优化  
可以看到记录大值和小值时是用max和min，考虑以此考虑合并
[说实话 我被这题搞吐了，气死我了😤]
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp_min, dp_max = [0] * len(nums), [0] * len(nums)  # dp_max记录正负交替乘法中的最大值
        dp_min[0], dp_max[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i],nums[i]*dp_max[i-1],dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i],nums[i]*dp_max[i-1],dp_min[i-1]*nums[i])
            # dp_max[i] = max(max(nums[i],nums[i]*dp_max[i-1]),dp_min[i-1]*nums[i])
            # dp_min[i] = min(min(nums[i],nums[i]*dp_max[i-1]),dp_min[i-1]*nums[i])

            # if nums[i] >= 0:
            #     dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i])
            #     dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i])
            # else:  # 此时nums[i]小于0
            #     dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
            #     dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res
```
观察上面的执行过程，其实我们使用到的dp_max和dp_min我们在计算过程中，都只使用到了最后一个，考虑进行空间优化  
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 
        res,pre_max,pre_min = nums[0],nums[0],nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
```

#### 打家劫舍
1.定义`dp[i][0,1]`为到第i个房子能取得的max_val，0代表不取，1代表取  
所以有 `dp[i][0]=max(dp[i-1][0],dp[i-1][1])`i不偷，那么i-1可偷可不偷  
`dp[i][1]=dp[i-1][0]+nums[i]`确定i偷，那么i-1不偷  
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0],dp[0][1] = 0, nums[0]
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])#i不偷，那么i-1可偷可不偷
            dp[i][1] = dp[i-1][0] + nums[i]#确定i偷，那么i-1不偷
        return max(dp[-1][0],dp[-1][1])
```
2.定义为dp[i]为i偷的时候的最大值，那么有：`dp[i]=max(dp[i-1],dp[i-2]+nums[i])`  
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[-1]
```
同样的在更新dp的时候也只是使用到了前面两个值，这里考虑空间优化
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre_max, cur_max = 0,0
        for i in range(len(nums)):
            # tmp = cur_max
            # cur_max = max(cur_max,nums+pre_max)
            # pre_max = tmp
            pre_max, cur_max = cur_max, max(cur_max,pre_max+nums[i])
        return cur_max
```

#### 买卖股票的最佳时机I
1.暴力解法 枚举每第i天买第j天抛除的所有可能，记录并返回最大值 (感觉是动态规划的一种)   
```python
from typing import List
class Solution:
    # 只能买卖一次
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力法 O(N^2)枚举第i天买入第j天卖出，记录最大值
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                res = max(res,prices[j]-prices[i])
        return res
``` 
2.动态规划 累计到第i天的最大收益为 第i-1天的最大收益值 和 第i天股票价格与当前历史最低股价差值 之间的最大值  
```python
from typing import List
class Solution:
    # 只能买卖一次
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0] * len(prices)
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            dp[i] = max(dp[i - 1], prices[i] - lowest)#状态转移只与前一个状态有关
        return dp[-1]
```
3. 看到labuladong的题解，里面对空间降维有这样一句描述 由于状态转化过程仅与前一个状态相关，所以可以用变量来存储  
对程序稍作修改，第一次难免会犯错  
```python
from typing import List
class Solution:
    # 只能买卖一次
    def maxProfit(self, prices: List[int]) -> int:
        pre, cur, lowest = 0,0,prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
              lowest = prices[i]
            cur = max(cur,prices[i]-lowest)
            # pre, cur = cur, max(cur, prices[i]-lowest)
            print(pre,cur)
        # return max(cur,pre)
        return cur
```
刚开始就想着那就拿两个数来存咯，然后在返回结果的时候就发现cur并不是最大的 打印pre，cur才知道转移过程写错了  
思考后，发现两个状态转移，一个变量就搞定了 所以有了上面的最终代码  

#### 买卖股票的最佳时机II 可以买卖股票多次
由于没有对买卖次数进行限制，我们可以找到股票图里所有上升段进行求和  
```python
from typing import List
class Solution:
    #可以买卖K次
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
```
#### 买卖股票的最佳时机III 只能买卖两次
考虑用二维数组做，dp[i][0,1,2,3]表示到i天买卖0-3次时 最大收益，这样定义状态的原因是因为限定了k=2，所以只有五种状态(原始状态+1)  
```python
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        #0未买入 1 买入一次 2 卖出一次 3 买入两次 4 卖出2次
        # dp = [[0]*len(prices) for _ in range(2*2+1)]
        dp = [[0]*5 for _ in range(len(prices))]
        dp[0][0] = dp[0][2] = dp[0][4] = 0
        dp[0][1] = dp[0][3] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = 0 #如果第i天没有买入，那么只可能i-1天没有买入
            #第i天买入一次，可能是i-1天未买i天买 或 第i-1天买i未买
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            #第i天买入一次卖出一次，可能是i-1天买入i天卖出或者i-1天已经买入卖出了
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            #第i天买入2次卖出1次，可能是i-1买卖(1,1)次，i天买入；也可能是是i-1天已经买卖(2,1)次
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            # 第i天买卖(2,2)可能是i-1天买卖(2,2)也可能是i-1天买卖(2,1)，i卖出
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        #最后手头没有股票剩余，实际收益最高
        return dp[-1][4]
```
很自然的看出，每一种状态的转移有着高度的相似性，我们考虑降维  
很显然这个状态转移，只与前一天相同状态dp[i-1][k]和前一天不同状态dp[i-1][k-1]有关，那么我们就能简化上述过程。  
【刚开始我也是去找别人的代码，发现状态转移稀奇古怪，】  
【要么是 对状态转移方程中对dp[i][1]和dp[i][3]做min操作，要么是做一些不直观的额外处理】  
【我想，既然是简化，那么状态转移过程应该与上述代码高度一致】  
【而不应该是在简化的状态转移方程中对dp[i][1]和dp[i][3]做min操作，也不应该做过多的边界处理】  
【按自己的思路对照上述方程，得如下】  
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        in_1,in_2 = float('-inf'),float('-inf')
        out_1,out_2 = 0,0
        for p in prices:
            in_1 = max(in_1,-p)
            out_1 = max(out_1, in_1 + p)
            in_2 = max(in_2,out_1 - p)
            out_2 = max(out_2, in_2 + p)
        return out_2
```
【我做题的时候就最烦我的思路和别人不一样，要改弦更张，记忆的细节就更多了】  
【你看，现在是不是与前面的逻辑一毛一样，方便记忆】  
但是对于后面k很大，比如就是三的时候，刚开始的思路是正确，但是就要写很多，这道题我还没做，做的时候再考虑该怎么处理~  

#### 买卖股票的最佳时机IV
```python
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def no_limit(prices):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        size = len(prices)
        if k > size / 2:
            return no_limit(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(size)]
        for i in range(size):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1] + prices[i])#前一天持有并卖掉
                    dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0] - prices[i])#前一天不持有，并买入
        return dp[size - 1][k][0]
```

#### 买卖股票的最佳时机V 冷冻期
实际上与前三题没什么不同，只是比第四题操作少一些，我们还是定义可能存在的状态  
```python
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0,1,2,3] 初始状态、买入、卖出、冷冻期
        # dp[i][0] = 0
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0] -p)
        # dp[i][2] = max(dp[i-1][2],dp[i-1][1] + p)
        # dp[i][3] = max(dp[i-1][3],dp[i-1][2])#要么是之前已经闲置，要么是正在闲置-->可以和初始状态合并
        if not prices: return 0
        dp = [[0]*3 for _ in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1] + prices[i])
        return dp[-1][2]
```
老样子，降维 但是直接降维会出错，要加中间状态  
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
            keep, in1, out1 = 0, -prices[0], 0
            for price in prices:
                new_keep = max(keep,out1)
                new_in1 = max(in1,keep-price)
                new_out1 = max(out1,in1+price)
                keep,in1,out1 = new_keep,new_in1,new_out1
            return out1
```

#### 买卖股票的最佳时机VI 手续费
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0],dp[i][1] 买入的最大值，卖出的最大值 
        dp = [[0,0] for _ in  range(len(prices))]
        dp[0][0],dp[0][1] = -prices[0] - fee,0
        # 每笔交易你只需要为支付一次手续费, 可以在买入的时候付，也可以在卖出的时候付，这里在买入的时候付
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0] , dp[i-1][1] - prices[i] - fee)#持股
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])#不持股
        return dp[-1][1]
```
降维  
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        in1, out1 = -prices[0] - fee, 0#在买入的时候付费
        for price in prices:
            in1 = max(in1, out1-price-fee)
            out1 = max(out1, in1 + price)
        return out1
```



