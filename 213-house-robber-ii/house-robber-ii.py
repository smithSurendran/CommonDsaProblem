class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_adj(nums):
            n= len(nums)
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]= max(nums[0], nums[1])

            for i in range(2,n):
                dp[i]= max(dp[i-2]+nums[i], dp[i-1])

            return dp[-1]   
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        first_house= rob_adj(nums[:-1])
        last_house= rob_adj(nums[1:])
        return max(first_house, last_house)
        
        