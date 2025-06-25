class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        max_len=0
        pal=""
        for i in range(len(s)):
            #for odd
            p1= expandAroundCenter(i,i)

            #for Even
            p2= expandAroundCenter(i, i+1)

            if len(p1)>max_len:
                max_len=len(p1)
                pal=p1
            if len(p2)>max_len:
                max_len=len(p2)
                pal=p2
        return pal 
        