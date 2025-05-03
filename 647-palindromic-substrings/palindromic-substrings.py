class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(st):
            return st==st[::-1]
        count=0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    #print(s[i:j])
                    count+=1
        return count

        