from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, it in enumerate(nums):
            x = target - it
            xIndx = cache.get(x, -1)
            if xIndx != -1:
                return [xIndx, index]
            cache[it] = index


if __name__ == "__main__":
    s = Solution()
    res = s.twoSum([2, 7, 11, 15], 9)
    print(res)

