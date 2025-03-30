class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(start, end, nums):
            if start==end:
                return nums[start]
            mid= (start+end)//2

            left_sum=helper(start,mid,nums)
            right_sum=helper(mid+1,end,nums)
            cross_sum=maxCrossSum(start,mid,end,nums)

            return max(left_sum, right_sum, cross_sum)

        def maxCrossSum(start, mid, end, nums):

            left_max=float('-inf')
            total=0

            for i in range( mid,start-1,-1):
                total+=nums[i]
                left_max= max(left_max, total)
            total=0
            right_max=float('-inf')
            for i in range(mid+1, end+1):
                total+=nums[i]
                right_max= max(right_max, total)
            return right_max+left_max
        return helper(0, len(nums)-1, nums) 
        