from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(r - l + 1, result)
                total -= nums[l]
                l += 1
        if result == len(nums) + 1:
            return 0
        return result


# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
if __name__ == "__main__":
    s = Solution()
    res = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(res)

    res = s.minSubArrayLen(4, [1, 4, 4])
    print(res)
