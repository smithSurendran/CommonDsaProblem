class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        mapped={')':'(', ']':'[', '}':'{'}

        for vp in s:
            if vp in mapped:
                if stack and stack[-1]==mapped[vp]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(vp)
        return not stack

                    


            