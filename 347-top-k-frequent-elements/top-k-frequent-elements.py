class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq= Counter(nums)
        result=[num for num, count in  heapq.nlargest(k, freq.items(), key=lambda x:x[1])]

        return result
        