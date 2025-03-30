class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        j=1
        left.append(1)
        right.append(1)
        for i in range(1,len(nums)):
            j*=nums[i-1]
            left.append(j)
        j=1
        for i in range(len(nums)-2,-1,-1):
            j*=nums[i+1]
            right.append(j)    
        
        result=[]
        for i in range(len(nums)):
            result.append(right.pop()*left[i])
        return result        

        