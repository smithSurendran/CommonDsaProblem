class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)

        dp=[ [False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        max_len=1
        start=0
        for end in range(n):
            for begin in range(end):
                if s[begin]==s[end]:
                    if end-begin==1 or dp[begin+1][end-1]:
                        dp[begin][end]=True

                        if (end-begin+1)>max_len:
                            max_len= (end-begin+1)
                            start=begin
        print(max_len)
        return s[start:start+max_len]

                