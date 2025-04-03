class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=0
        max_vm=0
        left=0
        right= len(height)-1

        while left<right:
            common_height=min(height[left], height[right])
            length= right-left
            max_vm= max(max_vm,common_height*length)
            
            if height[left]<height[right]:
                left+=1
            elif height[left]==height[right]:
                left+=1
                right-=1
            else:
             right-=1
        return max_vm
            

        