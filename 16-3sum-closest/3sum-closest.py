class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest=float('inf')
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right= len(nums)-1

            while left<right:
                total= nums[i]+nums[left]+nums[right]
                
                if total==target:
                    return total
                if abs(total-target) <abs(closest-target):
                    closest= total 
                if total<target:
                    left+=1
                else:
                    right-=1
            
        return closest
                
        