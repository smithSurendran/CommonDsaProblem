class Solution:
    def rob(self, nums: List[int]) -> int:
        def robadj(houses):
            n= len(houses)

            if n==1:
                return houses[0]
            if n==2:
                return max(houses[0], houses[1])
            
            dp=[0]*n
            dp[0]= houses[0]
            dp[1]= max(houses[0], houses[1])

            for i in range(2, n):
                dp[i]= max(dp[i-2]+houses[i], dp[i-1])
            
            return dp[-1]
        n= len(nums)
        if n==1:
            return nums[0]
        return max(robadj(nums[0:n-1]), robadj(nums[1:n]))
        