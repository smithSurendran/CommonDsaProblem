from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq= Counter(tasks)
        rounds=0
        for tasks, count in freq.items():
            if count<2:
                return -1
            rounds+=math.ceil(count/3)
        return rounds