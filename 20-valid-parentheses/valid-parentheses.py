class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'}':'{',']':'[',')':'('}

        stack=[]
        for i in range(len(s)):
            if stack and brackets.get(s[i])==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            
        if stack:
            return False
        return True
