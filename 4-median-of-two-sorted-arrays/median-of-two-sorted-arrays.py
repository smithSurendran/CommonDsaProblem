import heapq
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=[]
        min_heap=[]
        for num in nums1:
            heapq.heappush(min_heap, num)
        for num in nums2:
            heapq.heappush(min_heap, num)
        
        n= len(min_heap)

        med=np.median(min_heap)

        return med
        