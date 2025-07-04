class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals=sorted(intervals)
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            temp= result[-1]
            if intervals[i][0]<=temp[1]:
                result[-1][0]= min(result[-1][0], intervals[i][0])
                result[-1][1]= max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            #print(result)
        return result