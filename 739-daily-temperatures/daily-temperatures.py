class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        stack=[]

        answer=[0]*n

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev= stack.pop()
                answer[prev]=i-prev
            stack.append(i)
        return answer

        