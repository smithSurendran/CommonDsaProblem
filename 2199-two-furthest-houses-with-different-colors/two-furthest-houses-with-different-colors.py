class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        max_dist=0
        start= colors[0]
        n= len(colors)
        end= colors[n-1]
        if not colors:
            return 0
        for i in range(len(colors)):
            if colors[i]!=end and i>max_dist:
                max_dist=(n-1-i)
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=start and i>max_dist:
                max_dist=i
        return max_dist
        