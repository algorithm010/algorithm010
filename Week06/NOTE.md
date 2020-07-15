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






