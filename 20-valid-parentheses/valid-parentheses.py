class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        map={')':'(', '}':'{',']':'['}

        for c in s:
            if c in map.values():
                stack.append(c)
            if c in map:
                if not stack or stack[-1]!=map[c]:
                    return False
                stack.pop()
        return not stack

                    


            