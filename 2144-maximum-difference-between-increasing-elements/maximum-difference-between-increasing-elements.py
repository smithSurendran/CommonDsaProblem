class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num=-1
        min_num=float('inf')
        for num in nums:
            if num<min_num:
                min_num=num
            elif num-min_num>max_num:
                max_num= num-min_num
        return max_num if max_num>0 else -1
        