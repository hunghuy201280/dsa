from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                hset.remove(nums[L])
                L += 1
            if nums[R] in hset:
                return True
            hset.add(nums[R])
        return False


# Example 1:
# Input: nums = [1,2,3,1] , k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

if __name__ == "__main__":
    s = Solution()
    res = s.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(res)

    res = s.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(res)
    res = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(res)
