class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandFromCenter(l, r):
            freq=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                freq+=1
                l-=1
                r+=1
            return freq
        
        count=0
        for i in range(len(s)):
            #odd 
            count+= expandFromCenter(i,i)
            #even
            count+= expandFromCenter(i, i+1)

        return count
 