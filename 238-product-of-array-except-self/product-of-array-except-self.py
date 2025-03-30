class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        left=1
        for i in range(len(nums)):
            result.append(left)
            left*=nums[i]
        
        right=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result        

        