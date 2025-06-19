class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]

        k=0
        while k<len(intervals) and intervals[k][1]<newInterval[0]:
                result.append(intervals[k])
                k+=1
        while k<len(intervals) and intervals[k][0]<=newInterval[1]:
            newInterval[0]= min(intervals[k][0], newInterval[0])
            newInterval[1]= max(intervals[k][1], newInterval[1])
            print(newInterval)
            k+=1
        result.append(newInterval)



        while k<len(intervals):
            
            result.append(intervals[k])
            k+=1        

        return result

        
        