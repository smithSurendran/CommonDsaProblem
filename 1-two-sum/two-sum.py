from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair= defaultdict(int)
        result=[]
        for i in range(len(nums)):
            complement= target-nums[i]

            if complement in pair:
                index= pair[complement]
                result.append(index)
                result.append(i)
                break

            pair[nums[i]]=i   
        return result 

        