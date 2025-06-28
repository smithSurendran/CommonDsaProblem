class Solution:
    def reorganizeString(self, s: str) -> str:
        count= Counter(s)
        max_heap=[ (-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        result=[]
        while len(max_heap)>=2:
            freq1, char1= heapq.heappop(max_heap)
            freq2, char2= heapq.heappop(max_heap)

            result.append(char1)
            result.append(char2)

            if -freq1>1:
                heapq.heappush(max_heap, (freq1+1, char1))
            if -freq2>1:
                heapq.heappush(max_heap, (freq2+1, char2))
        if max_heap:
            freq, char= max_heap[0]
            if -freq>1:
                return ""
            result.append(char)
        return "".join(result)
        