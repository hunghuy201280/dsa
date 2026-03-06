from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        curSum = 0
        for r in range(len(arr)):

            if r - l + 1 > k:
                curSum -= arr[l]
                l += 1
            curSum += arr[r]
            if r - l + 1 == k and curSum / k >= threshold:
                res += 1

        return res


# Example 1:
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:
#
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
#
if __name__ == "__main__":
    s = Solution()
    res = s.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    print(res)

    res = s.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
    print(res)
