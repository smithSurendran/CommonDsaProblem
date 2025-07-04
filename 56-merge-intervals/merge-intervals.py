class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key=lambda x: x[0])

        result.append(intervals[0])

        for i in range(1,len(intervals)):
            last= result[-1]
            current= intervals[i]
            if last[1]>=current[0]:
                last[1]= max(last[1], current[1])
            else:
                result.append(intervals[i])
        return result