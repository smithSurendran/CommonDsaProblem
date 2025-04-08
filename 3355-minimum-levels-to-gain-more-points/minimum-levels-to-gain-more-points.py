class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n= len(possible)
        score= [-1 if x==0 else 1 for x in possible]
        total= sum(score)
        prefix=0

        for i in range(n-1):
            prefix+=score[i]
            bob_score= (total-prefix)
            if prefix> bob_score:
                return i+1
        return -1