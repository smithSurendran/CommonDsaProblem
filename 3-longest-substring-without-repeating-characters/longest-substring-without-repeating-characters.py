class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset= set()
        left=0
        max_substr=0
        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left+=1
            subset.add(s[right])
            max_substr= max(max_substr, len(subset))
        return  max_substr
            

