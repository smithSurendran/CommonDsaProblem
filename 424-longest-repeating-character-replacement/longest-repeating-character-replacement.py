class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len=0
        left=0
        count= defaultdict(int)
        max_freq=0
        for right in range(len(s)):
            count[s[right]]+=1
            max_freq= max(max_freq, count[s[right]])
            win_len= right-left+1

            while win_len-max_freq>k:
                count[s[left]]-=1
                left+=1
                win_len= right-left+1
            
            max_len= max(max_len, win_len)
        return max_len


