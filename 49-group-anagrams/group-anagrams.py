class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)

        for s in strs:
            key =tuple(sorted(s))
            anagram[key].append(s)
        return list(anagram.values())