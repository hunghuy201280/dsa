from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLc = 0
        s = set(nums)
        for n in nums:
            if n - 1 not in s:
                lc = 1
                while n + lc in s:
                    lc += 1
                maxLc = max(maxLc, lc)
        return maxLc


if __name__ == "__main__":
    s = Solution()
    res = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(res)
    res = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(res)
