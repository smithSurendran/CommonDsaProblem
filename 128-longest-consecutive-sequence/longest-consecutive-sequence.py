class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums= sorted(nums)
        max_count=1
        count=1
        prev= nums[0]
        for i in range(0,len(nums)):
            print("i ", i ,"count" ,count," ", nums[i], "prev ", prev )
            if nums[i]-1==prev:
                count+=1
                prev= nums[i]
            elif nums[i]==prev:
                continue    
            else:
                count=1
                prev= nums[i]
            
            
            max_count=max(max_count, count)    
        return max_count    
