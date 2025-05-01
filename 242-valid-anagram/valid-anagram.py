class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq= defaultdict(int)
        if len(t)!=len(s):
            return False
        for c in s:
            freq[c] +=1
        
        for w in t:
            if w in freq:
                freq[w]-=1
        
        return True if max(freq.values())==0 else False

        