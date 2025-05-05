class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        last= float('-inf')
        intervals.sort(key= lambda x:x[1])
        count=0
        for interval in intervals:
            if interval[0]>=last:
                last=interval[1]
            else:
                count+=1
        return count
        