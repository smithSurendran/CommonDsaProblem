class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pdt=nums[0]
        curr_max=curr_min=nums[0]
        for num in nums[1:]:
            if num<0:
                curr_min, curr_max= curr_max, curr_min
            
            curr_max= max(num, curr_max*num)

            curr_min= min(num, curr_min*num)

            max_pdt= max(max_pdt, curr_max)

        return max_pdt
            

