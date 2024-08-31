import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        maxHeap = []
        for key in count.keys():
            heapq.heappush(maxHeap, (-count[key], key))
        res = []
        while maxHeap and k:
            res.append(heapq.heappop(maxHeap)[1])
            k -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(res)
