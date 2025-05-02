class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_str=""
        for c in s:
            print(c)
            if c.isalnum():
                new_str+=c
        print(new_str)
        left =0
        right=len(new_str)-1
        while left<right:
            if new_str[left]!=new_str[right]:
                return False
            left+=1
            right-=1
        return True