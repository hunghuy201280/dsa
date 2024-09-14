from typing import List

from twisted.python.util import println


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            i = int((left + right) / 2)
            if target > nums[i]:
                left = i + 1

            elif target < nums[i]:
                right = i - 1

            else:
                return i

        if left >= len(nums):
            return len(nums)
        elif right < 0:
            return 0
        else:
            return left


if __name__ == "__main__":
    s = Solution()
    res = s.searchInsert([1], 0)
    println(res)
    res = s.searchInsert([1, 3, 5, 6], 0)
    println(res)
    res = s.searchInsert([1, 3, 5, 6], 5)
    println(res)
    res = s.searchInsert([1, 3, 5, 6], 2)
    println(res)
    res = s.searchInsert([1, 3, 5, 6], 7)
    println(res)
