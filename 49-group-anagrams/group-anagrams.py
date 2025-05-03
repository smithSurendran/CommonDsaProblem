class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)

        for word in strs:
            key =  ''.join(sorted(word))
            freq[key].append(word)
        
        print(freq.values())

        return list(freq.values())