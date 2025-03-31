class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #kadane Algorithm

        curr_max= nums[0]
        curr_min= nums[0]
        result= nums[0]

        for i in range(1,len(nums)):
            num= nums[i]

            if num<0:
                curr_min, curr_max= curr_max, curr_min
            curr_max= max(num, curr_max*num)
            curr_min= min(num, curr_min*num)

            result= max(curr_max, result)
        return result        