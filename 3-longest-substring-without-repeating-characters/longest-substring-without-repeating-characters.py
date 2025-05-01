class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq= defaultdict(int)

        right=left=0
        max_count=0
        for right in range(len(s)):
            freq[s[right]]+=1

            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            
            max_count=max(max_count, right-left+1)
        return max_count